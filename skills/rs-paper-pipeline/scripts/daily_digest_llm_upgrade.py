#!/usr/bin/env python3
from __future__ import annotations

import re
import json
import time
from collections import defaultdict
from pathlib import Path

from pipeline_config import get_repo, load_config
from services.digest_builder import build_digest_with_llm, extract_paper_date, validate_papers_for_digest

CONFIG = load_config()


def issue_data(issue) -> dict:
    return getattr(issue, "_rawData", None) or {}


def extract_arxiv_id(issue: dict) -> str | None:
    body = (issue or {}).get("body") or ""
    match = re.search(r"arxiv\.org/abs/([^\)\s]+)", body)
    return match.group(1).strip() if match else None


def load_open_issues(repo):
    issues = []
    for issue in repo.get_issues(state="open"):
        raw_data = getattr(issue, "_rawData", None) or {}
        if "pull_request" in raw_data:
            continue
        issues.append(issue)
    return issues


def collect_papers_by_date(issues):
    paper_by_date = defaultdict(list)
    digest_issue_by_date = {}

    for it in issues:
        raw = issue_data(it)
        t = raw.get("title") or it.title
        if "日报" not in t:
            paper_date = extract_paper_date(raw)
            if paper_date:
                paper_by_date[paper_date].append(raw)
        dm = re.search(r"日报\s*(\d{8})", t)
        if dm:
            digest_issue_by_date[dm.group(1)] = it

    return paper_by_date, digest_issue_by_date


def collect_expected_papers(repo, date: str, expected_arxiv_ids: list[str], retries: int = 6, wait_s: int = 5):
    expected = set(expected_arxiv_ids)
    if not expected:
        issues = load_open_issues(repo)
        paper_by_date, _ = collect_papers_by_date(issues)
        return sorted(paper_by_date.get(date, []), key=lambda x: x["number"])

    last_items = []
    for attempt in range(1, retries + 1):
        issues = load_open_issues(repo)
        matched = []
        found_ids = set()
        for issue in issues:
            raw = issue_data(issue)
            title = raw.get("title") or issue.title
            if "日报" in title:
                continue
            aid = extract_arxiv_id(raw)
            if aid in expected:
                matched.append(raw)
                found_ids.add(aid)
        if found_ids == expected:
            return sorted(matched, key=lambda x: x["number"])
        last_items = matched
        if attempt < retries:
            time.sleep(wait_s)

    missing = sorted(expected - {extract_arxiv_id(item) for item in last_items if extract_arxiv_id(item)})
    raise RuntimeError(f"digest paper set incomplete for {date}, missing arxiv ids: {', '.join(missing)}")


def main(target_date: str | None = None, stats_json: str | None = None):
    if not CONFIG.github_token:
        raise RuntimeError("Missing required environment variable: GITHUB_TOKEN")
    if not CONFIG.bailian_api_key:
        raise RuntimeError("Missing required environment variable: BAILIAN_API_KEY")

    repo = get_repo(CONFIG)

    stats_map = {}
    if stats_json:
        try:
            obj = json.loads(Path(stats_json).read_text(encoding="utf-8"))
            if isinstance(obj, dict) and obj.get("date"):
                stats_map[obj["date"]] = obj
        except Exception:
            pass

    issues = load_open_issues(repo)
    paper_by_date, digest_issue_by_date = collect_papers_by_date(issues)

    out_dir = CONFIG.temp_dir / "RS-PaperClaw" / "daily_reports"
    out_dir.mkdir(parents=True, exist_ok=True)

    dates = sorted(paper_by_date.keys())
    if target_date:
        dates = [d for d in dates if d == target_date]

    if not dates:
        print(f"NO_DIGEST_DATE target={target_date or 'ALL'}")
        return

    for date in dates:
        expected_ids = []
        if stats_map.get(date):
            expected_ids = (
                stats_map[date].get("successful_selected_arxiv_ids")
                or stats_map[date].get("selected_arxiv_ids")
                or []
            )
        papers = collect_expected_papers(repo, date, expected_ids) if expected_ids else sorted(paper_by_date[date], key=lambda x: x["number"])
        validation_errors = validate_papers_for_digest(papers)
        if validation_errors:
            raise RuntimeError(
                f"digest paper validation failed for {date}: " + " | ".join(validation_errors[:8])
            )
        md = build_digest_with_llm(
            date,
            papers,
            stats=stats_map.get(date),
        )
        (out_dir / f"{date}.md").write_text(md, encoding="utf-8")

        title = f"日报 {date}"
        labels = [date, "日报"]
        if date in digest_issue_by_date:
            digest_issue_by_date[date].edit(body=md, title=title, labels=labels)
            print(f"UPDATED digest issue {date} -> #{digest_issue_by_date[date].number}")
        else:
            ni = repo.create_issue(title=title, body=md, labels=labels)
            print(f"CREATED digest issue {date} -> #{ni.number}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--date", dest="date", help="仅生成指定日期日报，格式 YYYYMMDD")
    parser.add_argument("--stats-json", dest="stats_json", help="筛选统计 JSON 文件路径")
    args = parser.parse_args()

    main(target_date=args.date, stats_json=args.stats_json)
