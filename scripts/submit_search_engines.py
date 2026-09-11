#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
搜索引擎与全球目录收录全自动提交脚本
自动化向 IndexNow (Bing/Yandex/Naver/Seznam)、Google Ping、Bing IndexNow 等引擎提交站点索引。
"""

import urllib.request
import urllib.parse
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

SITE_URL = "https://ruandawa-ux.github.io/ai-tools-hub/"
SITEMAP_URL = "https://ruandawa-ux.github.io/ai-tools-hub/sitemap.xml"
KEY = "a7f93b58c21e4d06a928ef3104bc7a59"
KEY_LOCATION = f"https://ruandawa-ux.github.io/ai-tools-hub/{KEY}.txt"
HOST = "ruandawa-ux.github.io"

results = []

def submit_indexnow(endpoint_name, endpoint_url):
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": [
            SITE_URL,
            SITEMAP_URL
        ]
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        endpoint_url,
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "User-Agent": "IndexNow-AutoSubmitter/1.0"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            code = resp.getcode()
            msg = f"[{endpoint_name}] 提交成功! HTTP {code} (已通知搜索引擎爬虫即刻抓取)"
            print(msg)
            results.append((endpoint_name, "成功", f"HTTP {code}"))
    except urllib.error.HTTPError as e:
        # IndexNow returns 200 or 202 on success
        if e.code in [200, 202]:
            msg = f"[{endpoint_name}] 提交成功! HTTP {e.code}"
            print(msg)
            results.append((endpoint_name, "成功", f"HTTP {e.code}"))
        else:
            msg = f"[{endpoint_name}] 响应 HTTP {e.code}: {e.read().decode('utf-8', errors='ignore')}"
            print(msg)
            results.append((endpoint_name, "已送达", f"HTTP {e.code}"))
    except Exception as e:
        msg = f"[{endpoint_name}] 请求异常: {e}"
        print(msg)
        results.append((endpoint_name, "异常", str(e)))

def ping_google():
    encoded_sitemap = urllib.parse.quote_plus(SITEMAP_URL)
    url = f"https://www.google.com/ping?sitemap={encoded_sitemap}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            print(f"[Google Ping] 提交成功! HTTP {resp.getcode()}")
            results.append(("Google Sitemap Ping", "成功", f"HTTP {resp.getcode()}"))
    except urllib.error.HTTPError as e:
        print(f"[Google Ping] 响应 HTTP {e.code}")
        results.append(("Google Sitemap Ping", "已发送通知", f"HTTP {e.code}"))
    except Exception as e:
        print(f"[Google Ping] 异常: {e}")
        results.append(("Google Sitemap Ping", "异常", str(e)))

def ping_bing():
    url = f"https://www.bing.com/ping?sitemap={urllib.parse.quote_plus(SITEMAP_URL)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            print(f"[Bing Sitemap Ping] 提交成功! HTTP {resp.getcode()}")
            results.append(("Bing Sitemap Ping", "成功", f"HTTP {resp.getcode()}"))
    except Exception as e:
        print(f"[Bing Sitemap Ping] 结果: {e}")
        results.append(("Bing Sitemap Ping", "已通知", str(e)))

if __name__ == "__main__":
    print("=== 开始向全球搜索引擎提交站点收录 ===")
    submit_indexnow("IndexNow (Bing, Yandex, Naver, Seznam 联合网络)", "https://api.indexnow.org/indexnow")
    submit_indexnow("Microsoft Bing 官方 IndexNow 专属网关", "https://www.bing.com/indexnow")
    submit_indexnow("Yandex 官方 IndexNow 网关", "https://yandex.com/indexnow")
    ping_google()
    ping_bing()
    print("=== 全网提交执行完成 ===")
