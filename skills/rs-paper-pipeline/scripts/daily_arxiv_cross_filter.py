#!/usr/bin/env python3
from __future__ import annotations

"""
从 arXiv 拉取今天+昨天提交的论文，先按遥感关键词 OR 初筛，
再用 LLM 筛选“遥感 x 基础模型/计算机视觉/人工智能交叉”论文，
最后去重（已存在于 GitHub issues 的 arXiv id）并调用现有流程更新/创建 issue。
"""

import re
import json
from datetime import datetime
from pathlib import Path

from clients.arxiv_client import fetch_recent_candidates, has_remote_sensing_signal
from clients.github_ops import load_existing_arxiv_ids
from clients.llm_client import call_llm
from paper_processor import process_paper
from pipeline_config import get_repo, load_config
from services.filter_assets import load_ai_signal_patterns, render_filter_prompt

CONFIG = load_config()
AI_MATCH_PATTERNS = load_ai_signal_patterns()


def has_ai_signal(text: str) -> bool:
    return any(pattern.search(text) for pattern in AI_MATCH_PATTERNS)


def llm_cross_filter(candidates):
    if not candidates:
        return []

    payload = []
    for i, c in enumerate(candidates, 1):
        payload.append(f"[{i}] id={c['arxiv_id']} | title={c['title']} | abstract={c['abstract'][:500]}")

    prompt = render_filter_prompt(payload)
    out = call_llm(prompt, max_tokens=1200, timeout=180).strip()

    try:
        # 先尝试提取 ```json 代码块中的内容
        code_block = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", out)
        if code_block:
            json_str = code_block.group(1).strip()
        else:
            # 否则直接提取 JSON 数组
            json_str = re.search(r"\[[\s\S]*\]", out)
            json_str = json_str.group(0) if json_str else out
        arr = json.loads(json_str)
        keep = set(x.strip() for x in arr if isinstance(x, str))
        # 支持 LLM 返回的 ID 可能缺少 v1 后缀的情况
        def match_id(cid, keep_set):
            if cid in keep_set:
                return True
            # 尝试匹配无前缀版本
            cid_base = cid.replace("v1", "").replace("v2", "").rstrip("v")
            for k in keep_set:
                k_base = k.replace("v1", "").replace("v2", "").rstrip("v")
                if cid_base == k_base:
                    return True
            return False
        selected = [c for c in candidates if match_id(c["arxiv_id"], keep)]
        return [c for c in selected if has_remote_sensing_signal(f"{c['title']}\n{c['abstract']}")]
    except Exception:
        # LLM 解析失败时，保守降级：关键词交叉筛选
        out_items = []
        for c in candidates:
            text = f"{c['title']}\n{c['abstract']}"
            if has_remote_sensing_signal(text) and has_ai_signal(text):
                out_items.append(c)
        return out_items


def compact_item(item: dict[str, str]) -> dict[str, str]:
    return {
        "arxiv_id": item["arxiv_id"],
        "published": item["published"],
        "title": item["title"],
    }


def main(dry_run=False, days_back=2, stats_out: str | None = None, target_date: str | None = None):
    if not CONFIG.github_token:
        raise RuntimeError("Missing required environment variable: GITHUB_TOKEN")
    if not CONFIG.bailian_api_key:
        raise RuntimeError("Missing required environment variable: BAILIAN_API_KEY")

    repo = get_repo(CONFIG)

    if target_date:
        print(f"[1/5] 拉取指定日期 {target_date} 候选...")
        cands = fetch_recent_candidates(max_results=180, days_back=days_back, target_date=target_date)
    else:
        print(f"[1/5] 拉取最近 {days_back} 天候选...")
        cands = fetch_recent_candidates(max_results=180, days_back=days_back)
    cand_count = len(cands)
    print(f"  候选数: {cand_count}")

    print("[2/5] LLM 交叉筛选...")
    selected = llm_cross_filter(cands)
    selected_count = len(selected)
    print(f"  入选数: {selected_count}")

    print("[3/5] 读取 issue 去重...")
    existing = load_existing_arxiv_ids(repo)
    todo = [x for x in selected if x["arxiv_id"] not in existing]
    existing_count = len(selected) - len(todo)
    todo_count = len(todo)
    print(f"  已存在: {existing_count}，待处理: {todo_count}")

    stats = {
        "date": target_date or datetime.now().strftime("%Y%m%d"),
        "candidate_count": cand_count,
        "llm_selected_count": selected_count,
        "existing_count": existing_count,
        "todo_count": todo_count,
        "candidate_arxiv_ids": [x["arxiv_id"] for x in cands],
        "selected_arxiv_ids": [x["arxiv_id"] for x in selected],
        "existing_arxiv_ids": [x["arxiv_id"] for x in selected if x["arxiv_id"] in existing],
        "todo_arxiv_ids": [x["arxiv_id"] for x in todo],
        "candidate_items": [compact_item(x) for x in cands],
        "selected_items": [compact_item(x) for x in selected],
        "todo_items": [compact_item(x) for x in todo],
    }
    if stats_out:
        Path(stats_out).parent.mkdir(parents=True, exist_ok=True)
        Path(stats_out).write_text(json.dumps(stats, ensure_ascii=False), encoding="utf-8")

    if dry_run:
        print("[DRY RUN] 列表如下:")
        for x in todo:
            print(f"  - {x['arxiv_id']} | {x['published']} | {x['title'][:90]}")
        return

    print("[4/5] 提交 issue（不重复）...")
    for x in todo:
        aid = x["arxiv_id"]
        print(f"  -> 处理 {aid}")
        # 未指定 issue_number 时，process_paper 会按标题匹配更新；匹配不到则失败（当前 Phase1 策略）
        process_paper(aid, issue_number=None)

    print("[5/5] 完成")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--days", type=int, default=2, help="抓取最近 N 天的论文（默认2天）")
    parser.add_argument("--date", dest="date", help="抓取指定日期（YYYYMMDD）")
    parser.add_argument("--stats-out", dest="stats_out", help="输出统计 JSON 文件路径")
    args = parser.parse_args()

    main(dry_run=args.dry_run, days_back=args.days, stats_out=args.stats_out, target_date=args.date)
