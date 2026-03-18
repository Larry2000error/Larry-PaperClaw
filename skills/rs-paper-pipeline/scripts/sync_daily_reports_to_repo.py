#!/usr/bin/env python3
"""
将 GitHub 中“日报 YYYYMMDD” issues 同步到仓库 daily_reports 目录：
- daily_reports/YYYYMM/YYYYMMDD.md
- daily_reports/README.md（展示最新一天日报）
"""

import re

from clients.github_ops import cleanup_legacy_daily_reports, upsert_repo_file
from pipeline_config import get_repo, load_config

CONFIG = load_config()
BASE_DIR = "daily_reports"


def main():
    repo = get_repo(CONFIG)

    digest_issues = []
    for it in repo.get_issues(state="open"):
        m = re.fullmatch(r"日报\s*(\d{8})", (it.title or "").strip())
        if m:
            digest_issues.append((m.group(1), it))

    if not digest_issues:
        print("NO_DIGEST_ISSUES")
        return

    digest_issues.sort(key=lambda x: x[0])

    for date, issue in digest_issues:
        ym = date[:6]
        path = f"{BASE_DIR}/{ym}/{date}.md"
        body = (issue.body or "").strip() + "\n"
        upsert_repo_file(repo, path, body, f"sync daily report {date}")

    # 根目录 README 仅展示最近三天（最新在前）
    top3 = sorted(digest_issues, key=lambda x: x[0], reverse=True)[:3]
    lines = ["# Daily Reports", "", "最近三天日报（最新在前）：", ""]
    for date, issue in top3:
        ym = date[:6]
        body = (issue.body or "").strip()
        body = re.sub(
            rf"^#\s*日报\s*{date}\s*$",
            f"# [{date}](./{ym}/{date}.md)",
            body,
            count=1,
            flags=re.MULTILINE,
        )
        lines.append(body)
        lines.append("")
        lines.append("---")
        lines.append("")

    readme = "\n".join(lines).rstrip() + "\n"
    upsert_repo_file(repo, f"{BASE_DIR}/README.md", readme, f"update daily_reports README top3")

    cleanup_legacy_daily_reports(repo, BASE_DIR)

    print(f"DONE latest={top3[0][0]}")


if __name__ == "__main__":
    main()
