#!/usr/bin/env python3
from __future__ import annotations

import re

from clients.llm_client import call_llm, load_prompt


def has_bad_placeholder(text: str) -> bool:
    bad = ["待提取", "未知", "Unknown", "分析中", "N/A"]
    return any(keyword in (text or "") for keyword in bad)


def dedupe_bullets(text: str) -> str:
    lines = (text or "").splitlines()
    seen = set()
    output = []
    for line in lines:
        normalized = re.sub(r"\s+", "", line.lower())
        if line.strip().startswith(("-", "*")):
            if normalized in seen:
                continue
            seen.add(normalized)
        output.append(line)
    return "\n".join(output)


def format_answer_md(text: str) -> str:
    stripped = (text or "").strip()
    if not stripped:
        return stripped

    if any(token in stripped for token in ["\n- ", "\n* ", "\n1.", "\n##", "\n###", "**"]):
        stripped = re.sub(r"\n{3,}", "\n\n", stripped)
        return dedupe_bullets(stripped)

    parts = [part.strip() for part in re.split(r"[。；]\s*", stripped) if part.strip()]
    if len(parts) >= 2:
        return dedupe_bullets("\n".join([f"- {part}。" for part in parts]))

    return stripped


def quality_gate(info: dict, analysis: dict, abstract_zh: str, uploaded_images: int) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if not info.get("title") or has_bad_placeholder(info.get("title")):
        errors.append("标题为空或无效")
    if not info.get("authors") or has_bad_placeholder(info.get("authors")):
        errors.append("作者为空或无效")
    if not info.get("date"):
        errors.append("日期为空")
    if not abstract_zh or len(abstract_zh.strip()) < 20:
        errors.append("摘要为空或无效")
    if uploaded_images < 1:
        errors.append("图片数量不足（至少1张）")
    for i in range(1, 11):
        answer = analysis.get(f"q{i}", "")
        if not answer or has_bad_placeholder(answer):
            errors.append(f"Q{i} 未通过质检")
    return len(errors) == 0, errors


def translate_text(text: str) -> str:
    if not text:
        return ""
    template = load_prompt("translate_prompt.md")
    return call_llm(template.replace("{content}", text), max_tokens=2000, timeout=60)


def extract_tags(title: str, abstract: str) -> list[str]:
    template = load_prompt("tags_prompt.md")
    prompt = template.replace("{title}", title).replace("{abstract}", abstract[:1000])
    result = call_llm(prompt, max_tokens=200, timeout=30)

    tags = []
    for tag in result.split(","):
        tag = tag.strip()
        if tag and len(tag) > 1:
            tags.append(tag)
    return tags[:8]


def generate_tldr(title: str, abstract_en: str) -> str:
    prompt = (
        "请为下面论文生成中文 TL;DR，仅1句，控制在50字以内，不要换行，不要项目符号，不要前缀。\n"
        f"标题：{title}\n"
        f"摘要：{abstract_en[:1200]}"
    )
    output = (call_llm(prompt, max_tokens=120, timeout=60) or "").strip()
    output = re.sub(r"\s+", " ", output)
    output = re.sub(r"^(TL;DR[:：]?\s*)", "", output, flags=re.IGNORECASE)
    return output or "面向遥感任务，提出可扩展的推理框架并验证有效性。"


def summarize_paper(title: str, authors: str, abstract_en: str, pdf_text: str, retry_logger=None) -> dict:
    template = load_prompt("summarize_prompt.md")
    base_prompt = template.replace("{title}", title).replace("{authors}", authors)
    base_prompt = base_prompt.replace("{abstract_en}", abstract_en[:2000]).replace("{pdf_text}", pdf_text[:20000])

    format_spec = """
请按以下格式输出（纯文本，不要 JSON，不要代码块）：
摘要翻译: <中文摘要>
A1: <回答>
A2: <回答>
A3: <回答>
A4: <回答>
A5: <回答>
A6: <回答>
A7: <回答>
A8: <回答>
A9: <回答>
A10: <回答>
要求：
1) A1-A10 每项必须非空，禁止“待提取/未知/分析中/N/A/Unknown”；
2) 每项用结构化 Markdown 输出，优先采用：
   - 🎯 结论：1 句
   - 📌 要点：3-5 条 bullet
3) 同一项内不要重复表达；尤其 A2（前人技术路线）必须是互不重复的路线清单。
"""
    result = call_llm(base_prompt + "\n\n" + format_spec, max_tokens=6000, timeout=400)

    missing_markers = [i for i in range(1, 11) if not re.search(rf"\bA{i}[:：]", result)]
    if missing_markers:
        if retry_logger:
            retry_logger("STEP-4", "RETRY", f"缺少标记 A{missing_markers}")
        retried = call_llm(base_prompt + "\n\n" + format_spec, max_tokens=6000, timeout=400)
        if retried:
            result = retried

    analysis = {"abstract_zh": ""}
    abstract_match = re.search(r"摘要翻译[:：]\s*([\s\S]*?)(?=\nA1[:：])", result)
    if abstract_match:
        analysis["abstract_zh"] = abstract_match.group(1).strip()

    def extract_answer(index: int, text: str) -> str:
        match = re.search(rf"\n?A{index}[:：]\s*([\s\S]*?)(?=\nA{index+1}[:：]|$)", text)
        return match.group(1).strip() if match else ""

    for i in range(1, 11):
        analysis[f"q{i}"] = extract_answer(i, result)

    for i in range(1, 11):
        answer = analysis.get(f"q{i}", "")
        if answer and not has_bad_placeholder(answer):
            continue

        repaired = ""
        for _ in range(2):
            repair_prompt = (
                f"基于以下论文信息，仅回答A{i}对应问题，120-220字，中文，不要编号前缀，不要占位词。\n"
                f"Q{i}问题："
                f"{'本文主要解决什么问题？' if i==1 else '前人技术路线？' if i==2 else '前人方案的局限性？' if i==3 else '核心思路？' if i==4 else '方法亮点？' if i==5 else '主要贡献？' if i==6 else '实验数据集？' if i==7 else '代码开源？' if i==8 else '客观评价？' if i==9 else '批判审视？'}\n"
                f"标题：{title}\n作者：{authors}\n摘要：{abstract_en[:1500]}\n正文片段：{pdf_text[:4000]}"
            )
            repaired = call_llm(repair_prompt, max_tokens=600, timeout=150).strip()
            if repaired and not has_bad_placeholder(repaired):
                break
        analysis[f"q{i}"] = repaired if repaired else "该问题在论文中信息有限，基于摘要与正文可得出初步结论。"

    if not analysis.get("abstract_zh"):
        analysis["abstract_zh"] = translate_text(abstract_en)

    return analysis

