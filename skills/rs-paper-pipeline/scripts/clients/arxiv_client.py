#!/usr/bin/env python3
from __future__ import annotations

import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta
from urllib.error import HTTPError
from pathlib import Path

from pipeline_config import install_urllib_proxy, load_config
from services.filter_assets import load_rs_query_terms, load_rs_signal_patterns


CONFIG = load_config()
install_urllib_proxy()
RS_QUERY_TERMS = load_rs_query_terms()
RS_KEYWORDS = RS_QUERY_TERMS
RS_MATCH_PATTERNS = load_rs_signal_patterns()


def has_remote_sensing_signal(text: str) -> bool:
    return any(pattern.search(text) for pattern in RS_MATCH_PATTERNS)


def fetch_url_with_retry(url: str, retries: int = 4, timeout: int = 90) -> str:
    backoff = [2, 5, 10, 20]
    last_err = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": CONFIG.arxiv_user_agent})
            with urllib.request.urlopen(req, timeout=timeout) as response:
                return response.read().decode("utf-8", errors="ignore")
        except HTTPError as exc:
            last_err = exc
            if exc.code == 429:
                retry_after = exc.headers.get("Retry-After")
                if retry_after and retry_after.isdigit():
                    wait_s = int(retry_after)
                else:
                    wait_s = max(15, backoff[min(i, len(backoff) - 1)] * 3)
            else:
                wait_s = backoff[min(i, len(backoff) - 1)]
            if i == retries - 1:
                break
            time.sleep(wait_s)
        except Exception as exc:
            last_err = exc
            if i == retries - 1:
                break
            time.sleep(backoff[min(i, len(backoff) - 1)])
    raise last_err


def fetch_recent_candidates(
    max_results: int = 180,
    days_back: int = 2,
    target_date: str | None = None,
) -> list[dict[str, str]]:
    query_parts = []
    for keyword in RS_QUERY_TERMS:
        if " " in keyword:
            query_parts.append(f'all:"{keyword}"')
        else:
            query_parts.append(f"all:{keyword}")
    query = " OR ".join(query_parts)
    namespace = {"atom": "http://www.w3.org/2005/Atom"}

    if target_date:
        valid_days = {datetime.strptime(target_date, "%Y%m%d").date()}
    else:
        today = datetime.now().date()
        valid_days = {today - timedelta(days=i) for i in range(days_back)}

    items: list[dict[str, str]] = []
    seen: set[str] = set()
    page_size = min(max_results, 200)
    max_scan = 3000

    for start in range(0, max_scan, page_size):
        params = {
            "search_query": query,
            "start": start,
            "max_results": page_size,
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        url = f"{CONFIG.arxiv_api}?{urllib.parse.urlencode(params)}"
        xml_text = fetch_url_with_retry(url, retries=4, timeout=90)

        root = ET.fromstring(xml_text)
        entries = root.findall("atom:entry", namespace)
        if not entries:
            break

        min_page_date = None
        for entry in entries:
            arxiv_id = (entry.find("atom:id", namespace).text or "").strip().split("/")[-1]
            if arxiv_id in seen:
                continue
            seen.add(arxiv_id)

            title = (entry.find("atom:title", namespace).text or "").strip().replace("\n", " ")
            abstract = (entry.find("atom:summary", namespace).text or "").strip().replace("\n", " ")
            published = (entry.find("atom:published", namespace).text or "").strip()
            try:
                published_date = datetime.strptime(published[:10], "%Y-%m-%d").date()
            except Exception:
                continue

            if min_page_date is None or published_date < min_page_date:
                min_page_date = published_date

            if published_date not in valid_days:
                continue

            text = f"{title}\n{abstract}"
            if not has_remote_sensing_signal(text):
                continue

            items.append(
                {
                    "arxiv_id": arxiv_id,
                    "title": title,
                    "abstract": abstract,
                    "published": published[:10],
                }
            )

        if target_date and min_page_date and min_page_date < next(iter(valid_days)):
            break

    return items


def download_pdf(arxiv_id: str) -> tuple[Path | None, bool]:
    CONFIG.temp_dir.mkdir(parents=True, exist_ok=True)
    output = CONFIG.temp_dir / f"{arxiv_id}.pdf"
    mirrors = [
        f"https://arxiv.org/pdf/{arxiv_id}.pdf",
        f"https://export.arxiv.org/pdf/{arxiv_id}.pdf",
        f"https://ar5iv.org/pdf/{arxiv_id}",
    ]

    def threaded_download(url: str, parts: int = 4) -> bool:
        try:
            req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": CONFIG.arxiv_user_agent})
            with urllib.request.urlopen(req, timeout=20) as response:
                headers = {key.lower(): value for key, value in response.getheaders()}
            length = int(headers.get("content-length", "0"))
            accept_ranges = headers.get("accept-ranges", "")
            if length <= 0 or "bytes" not in accept_ranges.lower():
                return False

            chunk = length // parts
            ranges = []
            for i in range(parts):
                start = i * chunk
                end = (length - 1) if i == parts - 1 else ((i + 1) * chunk - 1)
                ranges.append((i, start, end))

            data_parts = [b""] * parts

            def fetch_part(idx: int, start: int, end: int):
                req = urllib.request.Request(
                    url,
                    headers={"User-Agent": CONFIG.arxiv_user_agent, "Range": f"bytes={start}-{end}"},
                )
                with urllib.request.urlopen(req, timeout=60) as response:
                    return idx, response.read()

            with ThreadPoolExecutor(max_workers=parts) as executor:
                futures = [executor.submit(fetch_part, i, start, end) for i, start, end in ranges]
                for future in as_completed(futures):
                    idx, part = future.result()
                    data_parts[idx] = part

            output.write_bytes(b"".join(data_parts))
            return output.exists() and output.stat().st_size > 0
        except Exception:
            return False

    for url in mirrors:
        try:
            if threaded_download(url, parts=4):
                return output, True
            with urllib.request.urlopen(url, timeout=60) as response:
                output.write_bytes(response.read())
            if output.exists() and output.stat().st_size > 0:
                return output, True
        except Exception:
            continue

    return None, False


def extract_abs_info(arxiv_id: str) -> dict[str, str]:
    url = f"https://arxiv.org/abs/{arxiv_id}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": CONFIG.arxiv_user_agent})
        with urllib.request.urlopen(req, timeout=30) as response:
            html = response.read().decode("utf-8")

        title_match = re.search(r'<h1[^>]*class="title[^"]*"[^>]*>(.*?)</h1>', html, re.DOTALL)
        title = re.sub(r"<.*?>", "", title_match.group(1)).strip() if title_match else "Unknown"
        title = re.sub(r"^Title:\s*", "", title)

        authors = []
        author_div = re.search(r'<div[^>]*class="authors"[^>]*>(.*?)</div>', html, re.DOTALL)
        if author_div:
            for name in re.findall(r"<a[^>]*>([^<]+)</a>", author_div.group(1)):
                name = name.strip()
                if name and len(name) > 2:
                    parts = name.split()
                    if len(parts) == 2:
                        name = f"{parts[1]} {parts[0]}"
                    authors.append(name)

        authors_str = ", ".join(authors[:5]) if authors else "待提取"
        if len(authors) > 5:
            authors_str += " et al."

        abstract_match = re.search(
            r'<blockquote[^>]*class="abstract[^"]*"[^>]*>.*?<span[^>]*>.*?</span>(.*?)</blockquote>',
            html,
            re.DOTALL,
        )
        abstract_en = re.sub(r"<.*?>", "", abstract_match.group(1)).strip() if abstract_match else ""

        date_match = re.search(r"\[Submitted on ([^\]]+)\]", html)
        if date_match:
            raw_date = date_match.group(1).strip()
            try:
                date = datetime.strptime(raw_date, "%d %b %Y").strftime("%Y-%m-%d")
            except Exception:
                date = datetime.now().strftime("%Y-%m-%d")
        else:
            date = datetime.now().strftime("%Y-%m-%d")

        return {
            "title": title,
            "authors": authors_str,
            "abstract_en": abstract_en,
            "date": date,
        }
    except Exception as exc:
        print(f"    ❌ 提取失败: {exc}")
        return {
            "title": "Unknown",
            "authors": "待提取",
            "abstract_en": "",
            "date": datetime.now().strftime("%Y-%m-%d"),
        }
