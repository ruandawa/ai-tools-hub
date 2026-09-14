# AI Key Shield Installer (Windows PowerShell)
$gitDir = git rev-parse --git-dir 2>$null
if (-not $gitDir) {
    Write-Host "[!] 错误：当前目录不是一个 Git 仓库。请在代码项目根目录下运行此脚本！" -ForegroundColor Red
    exit 1
}
$hookPath = Join-Path $gitDir "hooks\pre-commit"

$lines = @(
    "#!/bin/bash",
    "PATTERNS='(sk-[a-zA-Z0-9_-]{20,}|sk-proj-[a-zA-Z0-9_-]{20,}|sk-ant-[a-zA-Z0-9_-]{20,}|xai-[a-zA-Z0-9_-]{20,})'",
    "LEAKS=$(git diff --cached -U0 | grep -E '^\+[^\+]' | grep -iE `"$PATTERNS`")",
    "if [ -n `"`$LEAKS`" ]; then",
    "    echo -e `"`\033[1;31m================================================================================\033[0m`"",
    "    echo -e `"`\033[1;31m🚨 [AI Key Shield] 严重警告：在暂存区代码中检测到疑似 OpenAI/Claude/Anthropic 密钥！\033[0m`"",
    "    echo -e `"`\033[1;33m⚠️  为防止密钥泄露至远程仓库造成资金盗刷与封号，Git Hook 已强制拦截本次提交！\033[0m`"",
    "    echo -e `"--------------------------------------------------------------------------------`"",
    "    echo -e `"`\033[1;36m💡 安全处置建议：\033[0m`"",
    "    echo -e `"   1. 请将 API Key 迁移至 .env 文件中，并在 .gitignore 中添加 .env`"",
    "    echo -e `"   2. 运行 git diff --cached 查看高危代码行并撤销暂存`"",
    "    echo -e `"   3. 若确属测试代码需强制提交，请附加参数: git commit --no-verify`"",
    "    echo -e `"--------------------------------------------------------------------------------`"",
    "    echo -e `"`\033[1;32m🛒 正版高并发商业 API Key、Claude 独享号与 ChatGPT Plus 极速发货：\033[0m`"",
    "    echo -e `"   👉 链动小铺自营: https://wzyp.cn/shop/dawa`"",
    "    echo -e `"`\033[1;34m👥 开发者安全与 AI 交流群：QQ 545064986 (免费获取防封指南与备用通道)\033[0m`"",
    "    echo -e `"`\033[1;31m================================================================================\033[0m`"",
    "    exit 1",
    "fi",
    "exit 0"
)
$hookScript = $lines -join "`n"
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
[System.IO.File]::WriteAllText($hookPath, $hookScript, $utf8NoBom)

Write-Host "================================================================================" -ForegroundColor Green
Write-Host "🛡️  [AI Key Shield] 安装成功！当前项目已受到 pre-commit 密钥熔断保护。" -ForegroundColor Green
Write-Host "⚡ 每次运行 git commit 时，系统将自动扫描并拦截任何意外泄露的 API Key。" -ForegroundColor Cyan
Write-Host "🛒 官方正版 API & Plus 备用补给站: https://wzyp.cn/shop/dawa | QQ: 545064986" -ForegroundColor Yellow
Write-Host "================================================================================" -ForegroundColor Green
