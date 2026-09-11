#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
全球与国内 AI 导航站与目录自动提交脚本
自动化向全球 Ping 聚合网关 (Ping-o-Matic / Weblogs) 以及主流目录广播站点信息。
"""

import urllib.request
import urllib.parse
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

SITE_NAME = "AI TechHub 导航站"
SITE_URL = "https://ruandawa-ux.github.io/ai-tools-hub/"
FEED_URL = "https://ruandawa-ux.github.io/ai-tools-hub/rss.xml"
SHOP_URL = "https://wzyp.cn/shop/dawa"

def ping_pingomatic():
    """
    Ping-o-Matic 是全球最大的 Blog & 网站更新广播中心，
    一次 Ping 可自动通知 Google Blog Search、Weblogs.com、Feed Burner 等 20+ 个聚合平台。
    """
    params = {
        "title": SITE_NAME,
        "blogurl": SITE_URL,
        "rssurl": FEED_URL,
        "chk_weblogscom": "on",
        "chk_blogs": "on",
        "chk_feedburner": "on",
        "chk_syndic8": "on",
        "chk_newsgator": "on",
        "chk_myyahoo": "on",
        "chk_pubsubcom": "on",
        "chk_blogdigger": "on",
        "chk_audiogoat": "on"
    }
    url = f"https://pingomatic.com/ping/?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    try:
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            print(f"[Ping-O-Matic 全球广播] 提交成功! HTTP {resp.getcode()} (已广播至全球 20+ 个内容索引库)")
            return True
    except Exception as e:
        print(f"[Ping-O-Matic 全球广播] 通知结果: {e}")
        return False

def ping_rpc_weblogs():
    """
    通过 XML-RPC 标准协议向 Weblogs.com 发起更新通知
    """
    xml_data = f"""<?xml version="1.0"?>
<methodCall>
  <methodName>weblogUpdates.ping</methodName>
  <params>
    <param><value>{SITE_NAME}</value></param>
    <param><value>{SITE_URL}</value></param>
  </params>
</methodCall>
"""
    req = urllib.request.Request(
        "http://rpc.weblogs.com/RPC2",
        data=xml_data.encode("utf-8"),
        headers={"Content-Type": "text/xml"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"[Weblogs.com RPC] 广播成功! HTTP {resp.getcode()}")
            return True
    except Exception as e:
        print(f"[Weblogs.com RPC] 结果: {e}")
        return False

if __name__ == "__main__":
    print("=== 开始向全球内容目录与广播网关提交站点 ===")
    ping_pingomatic()
    ping_rpc_weblogs()
    print("=== 全球广播提交执行完毕 ===")
