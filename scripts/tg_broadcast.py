#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Telegram 自动广播推流脚本
用于向 Telegram 频道 / 交流群全自动推送大娃AI小店 (wzyp.cn/shop/dawa) 的每日特惠与库存通知。

使用方法:
  python tg_broadcast.py --token "YOUR_BOT_TOKEN" --chat-id "@your_channel_or_chat_id" --message "自定义内容(可选)"
"""

import sys
import json
import argparse
import urllib.request
import urllib.parse

DEFAULT_PROMO_MESSAGE = """🔥 <b>【2026 前沿 AI 生产力工具特惠通知】</b>

🚀 <b>全品类 24 小时全自动发卡现货上架：</b>
• <b>Cursor Pro 独享月卡/年卡</b>：编程提速 5 倍，海外原卡直充
• <b>Claude 3.7 Pro / Sonnet</b>：深度逻辑推理天花板，独享车位
• <b>ChatGPT-4o / Plus 会员</b>：官方正规通道，拒绝黑卡封禁
• <b>各大模型高并发 API 额度</b>：支持 OpenAI / Claude 聚合中转

⚡ <b>24H 自助直达下单通道：</b>
👉 官网小店：<a href="https://wzyp.cn/shop/dawa">wzyp.cn/shop/dawa</a>
👉 开源导航：<a href="https://ruandawa-ux.github.io/ai-tools-hub/">ruandawa-ux.github.io/ai-tools-hub</a>

🛡️ <i>正规实体卡渠道 · 全品类带首登质保售后 · 极速秒发无需等待</i>
"""

def send_telegram_message(bot_token: str, chat_id: str, text: str):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=15) as response:
            result = json.loads(response.read().decode("utf-8"))
            if result.get("ok"):
                print("[SUCCESS] 消息已成功推送至 Telegram 频道/群组！")
                return True
            else:
                print(f"[ERROR] 推送失败: {result}")
                return False
    except Exception as e:
        print(f"[EXCEPTION] 网络请求异常: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Telegram 自动广播推流脚本")
    parser.add_argument("--token", required=True, help="Telegram Bot Token (从 @BotFather 获取)")
    parser.add_argument("--chat-id", required=True, help="频道用户名如 @your_channel 或数字群组 ID")
    parser.add_argument("--message", default=DEFAULT_PROMO_MESSAGE, help="要推送的 HTML 格式消息")
    
    args = parser.parse_args()
    send_telegram_message(args.token, args.chat_id, args.message)

if __name__ == "__main__":
    main()
