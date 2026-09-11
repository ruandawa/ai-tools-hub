#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
百度搜索资源平台 (Baidu Search Resource Platform) 自动推流脚本
用于将独立站和发卡小店链接主动推送到百度爬虫库。

使用方法:
  python baidu_submit.py --token "你的百度推送Token"
"""

import sys
import argparse
import urllib.request

URLS = [
    "https://ruandawa-ux.github.io/ai-tools-hub/",
    "https://ruandawa-ux.github.io/ai-tools-hub/sitemap.xml"
]

def submit_to_baidu(site_domain: str, token: str):
    api_url = f"http://data.zz.baidu.com/urls?site={site_domain}&token={token}"
    data = "\n".join(URLS).encode("utf-8")
    req = urllib.request.Request(
        api_url,
        data=data,
        headers={"Content-Type": "text/plain"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            result = resp.read().decode("utf-8")
            print(f"[SUCCESS] 百度主动推送成功: {result}")
            return True
    except Exception as e:
        print(f"[ERROR] 百度推送失败: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="百度搜索引擎快速推流脚本")
    parser.add_argument("--token", required=True, help="百度搜索资源平台的 API 准入密钥 (Token)")
    parser.add_argument("--site", default="https://ruandawa-ux.github.io", help="在百度登记的站点域名")
    args = parser.parse_args()
    submit_to_baidu(args.site, args.token)
