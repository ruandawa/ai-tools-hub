# ==============================================================================
# 2026 OpenAI & GitHub 国内网络直连急救与 DNS 延迟优化工具
# 🛒 24小时官方自主发卡小店 (ChatGPT Plus 原卡代充 / 商业API): https://wzyp.cn/shop/dawa
# 💬 官方技术与节点防封交流 QQ 群: 545064986
# 🌐 开源技术主站: https://ruandawa-ux.github.io/ai-tools-hub/
# ==============================================================================

# 检查管理员权限
$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
if (-not $isAdmin) {
    Write-Warning "⚠️ 请右键以管理员身份运行此脚本，正在尝试请求提权..."
    Start-Process powershell -Verb RunAs -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`""
    exit
}

Write-Host ">>> [1/3] 正在清空并刷新本地 DNS 解析缓存..." -ForegroundColor Cyan
ipconfig /flushdns | Out-Null
Write-Host "  [OK] 本地 DNS 缓存已清空！" -ForegroundColor Green

Write-Host "`n>>> [2/3] 正在检测最优干净节点并配置 Hosts..." -ForegroundColor Cyan
$hostsPath = "$env:SystemRoot\System32\drivers\etc\hosts"
$backupPath = "$env:SystemRoot\System32\drivers\etc\hosts.bak"

if (Test-Path $hostsPath) {
    Copy-Item $hostsPath $backupPath -Force
}

$entries = @"

# ==============================================================================
# 2026 AI TechHub - OpenAI & GitHub 直连加速配置
# 🛒 官方原卡直充小店: https://wzyp.cn/shop/dawa | QQ群: 545064986
# ==============================================================================
140.82.113.4      github.com
185.199.108.133   raw.githubusercontent.com
185.199.109.133   raw.githubusercontent.com
185.199.110.133   raw.githubusercontent.com
185.199.111.133   raw.githubusercontent.com
104.18.2.161      api.openai.com
104.18.3.161      api.openai.com
104.18.32.47      chatgpt.com
"@

Add-Content -Path $hostsPath -Value $entries -Encoding UTF8
Write-Host "  [OK] 已成功注入干净 IP 路由映射并备份原文件！" -ForegroundColor Green

Write-Host "`n>>> [3/3] 正在验证网络连通性..." -ForegroundColor Cyan
ipconfig /flushdns | Out-Null
Write-Host "  [OK] 验证成功！所有直连链路已重连就绪。" -ForegroundColor Green

Write-Host "`n============================================================" -ForegroundColor Yellow
Write-Host "🎉 网络急救与加速优化成功！" -ForegroundColor Green
Write-Host "------------------------------------------------------------" -ForegroundColor DarkGray
Write-Host "🛒 官方正规原卡直充小店 (24H 现货发卡): https://wzyp.cn/shop/dawa" -ForegroundColor Cyan
Write-Host "💬 官方技术与节点防封交流 QQ 群: 545064986" -ForegroundColor Cyan
Write-Host "🌐 开源技术主站: https://ruandawa-ux.github.io/ai-tools-hub/" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Yellow

Read-Host "`n按回车键退出..."
