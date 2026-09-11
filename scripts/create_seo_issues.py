#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub 高频报错与搜索截流 Issue 批量创建脚本
利用开发者在 Google 频繁搜索报错红字的刚需，通过高权重 GitHub Issue 实现霸屏截流。
"""

import subprocess
import os

ISSUES = [
    {
        "title": "[SOLVED] OpenAI / ChatGPT: 'Your card has been declined' (国内双币信用卡支付失败 / 绑卡被拒 2026 最新官方通道与解决方案)",
        "body": """### 常见报错现象
在国内尝试开通或升级 **ChatGPT Plus (GPT-4o)** 时，Stripe 支付网关经常弹出如下红字报错：
> **"Your card has been declined."**
> 或 **"We are unable to authenticate your payment method. Please choose a different payment method and try again."**

---

### 产生原因深度解析（95% 用户被卡住的核心）
1. **Stripe 地区反欺诈风控（Radar 拦截）**：OpenAI 官方委托的 Stripe 支付通道对发卡行 BIN 码有极高风控，国内发行的 Visa / MasterCard / 运通卡绝大多数被系统直接拉黑；
2. **IP 伪装度与账单地址冲突**：使用公共机场或数据中心 IP（如 AWS / 阿里云香港）访问支付页面，风控直接触发 403；
3. **低价黑卡的致命陷阱**：网上部分二道贩子兜售的 30~50 元代充采用盗刷卡（料卡），发卡行拒付后官方 100% 连环封号封设备。

---

### 终极解决方案与正规直充通道

如果你手头没有经过实名验证的海外实体银行卡，或者不想承担自行绑卡被拒、账号被封的风险，可通过技术团队维护的官方正规自营发卡站开通：

👉 **[24小时官方自主发卡小站：wzyp.cn/shop/dawa](https://wzyp.cn/shop/dawa)**

#### 服务保障：
- ✅ **正规海外实体卡通道**：坚持一手合法实体渠道充值，支持国内自有普通老号直接原卡升级，零封号风险；
- ✅ **成品独享高权重老号现货**：含官方原生邮箱，修改密码后 100% 归个人独享；
- ✅ **全自动秒发**：系统 24 小时全自动出卡密与使用指引，无需人工值守；
- ✅ **官方首登质保售后**：任何环境登录问题提供专人协助。

---
💬 **官方技术交流与售后 QQ 群**：**545064986**  
🌐 **全球开源导航站**：https://ruandawa-ux.github.io/ai-tools-hub/
"""
    },
    {
        "title": "[SOLVED] Cursor: 'Too many free trials on this machine' (设备识别码已被锁定 / 2026 最新重置与独享开通指南)",
        "body": """### 常见报错现象
使用 Cursor 编程时，突然弹出限制弹窗：
> **"Too many free trials on this machine. Please upgrade to Pro."**
即便更换了新邮箱注册登录，依然无法继续使用免费试用。

---

### 产生原因深度解析
Cursor 官方对本地硬件进行了深度指纹采集，存储在本地的 Machine ID、Mac 网卡哈希以及 Device UUID 均已被服务端记录进黑名单。

---

### 解决方案与快速通道

#### 方案 A：开发者手动重置
1. 彻底退出 Cursor 进程；
2. 打开配置文件：
   - Windows: `%APPDATA%\\Cursor\\User\\globalStorage\\storage.json`
   - macOS: `~/Library/Application Support/Cursor/User/globalStorage/storage.json`
3. 修改 `telemetry.machineId`、`telemetry.macMachineId`、`telemetry.devDeviceId` 为随机 64 位哈希；
4. 更换干净新邮箱登录。

#### 方案 B：直接开通官方正规独享 Pro（告别频繁重置折腾）
如果你正在赶项目进度，不想每次被锁设备、折腾环境变量，建议直接开通官方正规独享 Pro 或原卡直充：

👉 **[24小时官方直充小店：wzyp.cn/shop/dawa](https://wzyp.cn/shop/dawa)**
- ⚡ 独享月卡/年卡即时下发，正规原卡充值稳定不封
- 🛡️ 全品类带质保售后，专人解答

---
💬 **官方技术交流 QQ 群**：**545064986**  
🌐 **开源项目地址**：https://github.com/ruandawa-ux/ai-tools-hub
"""
    },
    {
        "title": "[SOLVED] Claude 3.7: 'Your account has been disabled / Access Denied' (账号被封申诉技巧与原生住宅IP通道)",
        "body": """### 常见报错现象
访问或登录 Claude 官网时，页面显示：
> **"Your account has been disabled"**
> 或 **"Access Denied (Error code 1020)"**

---

### 核心诱因解析
Anthropic 的风控机制极其严苛：
1. **公共节点污染**：99% 的机场节点存在多人同时高频并发访问，被 Cloudflare 直接标记为机器人爬虫；
2. **跨时区频繁漂移**：短时间内在不同国家地区切换 IP，触发防盗号锁定；
3. **黑料充值遭封退**：低价代充被发卡行拒付。

---

### 申诉技巧与稳定独享通道
1. **申诉方式**：向 `support@anthropic.com` 发送英文申诉信，说明自己是正当科研开发者，请求解封；
2. **若无法解封**，请务必使用干净的原生住宅 IP 重新注册，或通过正规独享车位开通：

👉 **[24小时官方自主发卡通道：wzyp.cn/shop/dawa](https://wzyp.cn/shop/dawa)**
- ✅ 原卡直充，支持 Claude 3.7 Sonnet 满血推理
- ✅ 独享成品号，带首登质保售后保障

---
💬 **官方技术与售后交流 QQ 群**：**545064986**
"""
    }
]

def create_issues():
    temp_file = "temp_issue_body.txt"
    for item in ISSUES:
        title = item["title"]
        body = item["body"]
        with open(temp_file, "w", encoding="utf-8") as f:
            f.write(body)
        
        cmd = [
            "gh", "issue", "create",
            "-R", "ruandawa-ux/ai-tools-hub",
            "--title", title,
            "--body-file", temp_file
        ]
        print(f"[*] 正在创建 Issue: {title} ...")
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
        if result.returncode == 0:
            print(f"[SUCCESS] 创建成功: {result.stdout.strip()}")
        else:
            print(f"[ERROR] 创建失败: {result.stderr.strip()}")
            
    if os.path.exists(temp_file):
        os.remove(temp_file)

if __name__ == "__main__":
    create_issues()
