#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import subprocess
import urllib.request

from pipeline_config import build_runtime_env, install_urllib_proxy, load_config


CONFIG = load_config()
install_urllib_proxy()


def resolve_openclaw_cmd() -> list[str] | None:
    if CONFIG.openclaw_bin:
        resolved = shutil.which(CONFIG.openclaw_bin)
        if resolved:
            return [resolved]
    resolved = shutil.which("openclaw", path=build_runtime_env().get("PATH"))
    if resolved:
        return [resolved]
    return None


def has_available_notify_channel() -> bool:
    if CONFIG.dingtalk_webhook:
        return True
    if CONFIG.feishu_target and resolve_openclaw_cmd():
        return True
    return False


def send_feishu_message(text: str, timeout: int = 60) -> bool:
    if not CONFIG.feishu_target:
        return False
    cmd_prefix = resolve_openclaw_cmd()
    if not cmd_prefix:
        return False
    cmd = cmd_prefix + [
        "message",
        "send",
        "--channel",
        "feishu",
        "--target",
        CONFIG.feishu_target,
        "--message",
        text,
    ]
    subprocess.run(cmd, check=True, env=build_runtime_env(), cwd=CONFIG.root_dir, timeout=timeout)
    return True


def send_dingtalk_markdown(title: str, text: str, timeout: int = 30) -> bool:
    if not CONFIG.dingtalk_webhook:
        return False
    ding_title = f"RS {title}".strip()
    ding_text = text if "RS" in text else f"RS\n\n{text}"
    payload = {
        "msgtype": "markdown",
        "markdown": {
            "title": ding_title,
            "text": ding_text,
        },
    }
    req = urllib.request.Request(
        CONFIG.dingtalk_webhook,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        body = json.loads(response.read().decode("utf-8"))
    if body.get("errcode") not in (0, "0", None):
        raise RuntimeError(f"DingTalk webhook failed: {body}")
    return True
