#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
国内主流办公协作群 (企业微信 / 飞书 / 钉钉) 机器人自动化推流脚本
支持向开发团队群、极客交流群一键广播 AI 生产力工具特惠与独立站动态。

使用方法:
  # 企业微信群机器人:
  python wecom_feishu_dingtalk.py --type wecom --webhook "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxxx"

  # 飞书群机器人:
  python wecom_feishu_dingtalk.py --type feishu --webhook "https://open.feishu.cn/open-apis/bot/v2/hook/xxxx"

  # 钉钉群机器人:
  python wecom_feishu_dingtalk.py --type dingtalk --webhook "https://oapi.dingtalk.com/robot/send?access_token=xxxx"
"""

import argparse
import json
import urllib.request

TITLE = "🚀 2026 前沿 AI 生产力工具速递与正规通道"
TEXT_CONTENT = """### 🔥 2026 前沿 AI 生产力工具特惠与环境指南

近期各开发团队都在加速接入前沿 AI 辅助工具，为解决外币卡门槛与封号痛点，推荐以下正规稳定通道：

- **Cursor Pro 编程利器**：Claude 3.7 / GPT-4o 深度补全，原卡直充/独享车位
- **Claude 3.7 Pro / Sonnet**：推理长文本天花板，原生住宅IP养号，首登质保
- **ChatGPT-4o / Plus 会员**：官方原卡代充，彻底拒绝黑卡与拒付封禁
- **各大模型高并发 API 额度**：支持 OpenAI / Claude 聚合调用与极速下发

---
🛒 **24小时全自动发卡小店**：[点击进入自主下单](https://wzyp.cn/shop/dawa)
🌐 **开源极客技术导航站**：[https://ruandawa-ux.github.io/ai-tools-hub/](https://ruandawa-ux.github.io/ai-tools-hub/)
💬 **官方技术与售后交流 QQ 群**：**545064986**
"""

def send_wecom(webhook_url: str):
    payload = {
        "msgtype": "markdown",
        "markdown": {
            "content": TEXT_CONTENT
        }
    }
    return post_json(webhook_url, payload, "企业微信")

def send_feishu(webhook_url: str):
    payload = {
        "msg_type": "interactive",
        "card": {
            "header": {
                "title": {"tag": "plain_text", "content": TITLE},
                "template": "indigo"
            },
            "elements": [
                {
                    "tag": "markdown",
                    "content": TEXT_CONTENT
                }
            ]
        }
    }
    return post_json(webhook_url, payload, "飞书")

def send_dingtalk(webhook_url: str):
    payload = {
        "msgtype": "markdown",
        "markdown": {
            "title": TITLE,
            "text": TEXT_CONTENT
        }
    }
    return post_json(webhook_url, payload, "钉钉")

def post_json(url: str, payload: dict, platform_name: str):
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"}
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            res = resp.read().decode("utf-8")
            print(f"[{platform_name}] 广播成功: {res}")
            return True
    except Exception as e:
        print(f"[{platform_name}] 广播异常: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="企业微信/飞书/钉钉群机器人自动化广播推流工具")
    parser.add_argument("--type", choices=["wecom", "feishu", "dingtalk"], required=True, help="机器人类型")
    parser.add_argument("--webhook", required=True, help="自定义机器人的完整 Webhook 地址")
    args = parser.parse_args()

    if args.type == "wecom":
        send_wecom(args.webhook)
    elif args.type == "feishu":
        send_feishu(args.webhook)
    elif args.type == "dingtalk":
        send_dingtalk(args.webhook)

if __name__ == "__main__":
    main()
