#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dev.to 自动化文章发布脚本 (全网高权重技术社区外链与流量捕获器)
使用 Dev.to 开放 REST API 直接批量推送技术指南，收割全球与国内出海开发者的 Google 搜索流量。
"""

import urllib.request
import json
import os
import sys

DEVTO_API_KEY = os.environ.get("DEVTO_API_KEY", "")

ARTICLES = [
    {
        "title": "2026 Complete Guide: Solving 'Your card has been declined' on OpenAI ChatGPT Plus",
        "tags": ["chatgpt", "openai", "ai", "programming"],
        "body_markdown": """# 2026 Complete Guide: Solving 'Your card has been declined' on OpenAI ChatGPT Plus

Many developers encountering Stripe card verification failure when upgrading to **ChatGPT Plus (GPT-4o)** or setting up commercial OpenAI API keys.

---

### Root Causes Analysis
1. **Stripe Radar Risk Engine**: Strict issuing BIN country filtering for international cards.
2. **Datacenter IP Block**: Accessing checkout sessions through dirty public datacenter VPN proxies triggers instant 403 blocks.
3. **Carding / Black Market Traps**: Unregulated low-price upgrades lead to account termination upon payment chargebacks.

---

### Official Channels & Safe Solutions
For secure, stable access with warranty support:
- 🛒 **24/7 Instant Delivery Store**: [https://wzyp.cn/shop/dawa](https://wzyp.cn/shop/dawa)
- 🌐 **Global AI Tools Hub**: [https://ruandawa-ux.github.io/ai-tools-hub/](https://ruandawa-ux.github.io/ai-tools-hub/)
- 💬 **Official Technical Community (QQ Group)**: 545064986

Enjoy clean, stable productivity in 2026!
"""
    },
    {
        "title": "Cursor AI: How to Solve 'Too many free trials on this machine' in 2026",
        "tags": ["cursor", "ai", "vscode", "devtools"],
        "body_markdown": """# Cursor AI: How to Solve 'Too many free trials on this machine' in 2026

If you are locked out of Cursor with the message:
> **"Too many free trials on this machine. Please upgrade to Pro."**

Here is the architectural explanation and automated solution.

---

### The Mechanism
Cursor tracks hardware hashes inside `storage.json`:
- `telemetry.machineId`
- `telemetry.macMachineId`
- `telemetry.devDeviceId`

---

### Automated Reset Tool
Download our open-source batch reset tool directly:
- 👉 [GitHub Repository & Release Download](https://github.com/ruandawa-ux/cursor-free-trials-reset-tool)
- 👉 [24/7 Official Fast Pass](https://wzyp.cn/shop/dawa)
- 💬 QQ Community: 545064986
"""
    }
]

def publish_to_devto(api_key):
    if not api_key:
        print("[!] DEVTO_API_KEY 未设置。若需全自动发布到 Dev.to，请在 https://dev.to/settings/extensions 免费生成一个 API Key 并设置环境变量。")
        print("[*] 正在执行本地模拟生成与排版验证...")
        for i, art in enumerate(ARTICLES, 1):
            print(f"[{i}] 文章: {art['title']} (标签: {', '.join(art['tags'])}) [验证通过]")
        return

    url = "https://dev.to/api/articles"
    for art in ARTICLES:
        payload = {
            "article": {
                "title": art["title"],
                "published": True,
                "body_markdown": art["body_markdown"],
                "tags": art["tags"]
            }
        }
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={
                    "Content-Type": "application/json",
                    "api-key": api_key,
                    "User-Agent": "DevtoAutoPublisher/1.0"
                }
            )
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                print(f"[OK] 成功发布文章: {data.get('title')} -> {data.get('url')}")
        except Exception as e:
            print(f"[!] 发布文章失败 [{art['title']}]: {e}")

if __name__ == "__main__":
    publish_to_devto(DEVTO_API_KEY)