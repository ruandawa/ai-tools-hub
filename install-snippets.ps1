# ==============================================================================
# 2026 AI 生产力代码片段 (VS Code / Cursor / Windsurf) 一键自动安装脚本
# 🛒 官方发卡小店: https://wzyp.cn/shop/dawa | QQ群: 545064986
# ==============================================================================

Write-Host ">>> 正在为您的开发环境安装 2026 AI 生产力代码片段库..." -ForegroundColor Cyan

$snippetUrl = "https://ruandawa-ux.github.io/ai-tools-hub/snippets/ai-productivity.code-snippets"
$snippetContent = Invoke-RestMethod -Uri $snippetUrl -UseBasicParsing

$targets = @(
    "$env:APPDATA\Code\User\snippets",
    "$env:APPDATA\Cursor\User\snippets",
    "$env:APPDATA\Windsurf\User\snippets"
)

$installedCount = 0

foreach ($dir in $targets) {
    if (Test-Path (Split-Path $dir -Parent)) {
        if (!(Test-Path $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }
        $targetFile = Join-Path $dir "ai-productivity.code-snippets"
        $snippetContent | Set-Content -Path $targetFile -Encoding UTF8
        Write-Host "  [OK] 成功安装至: $dir" -ForegroundColor Green
        $installedCount++
    }
}

Write-Host "`n============================================================" -ForegroundColor Yellow
Write-Host "🎉 安装完成！在 VS Code / Cursor 中输入 'ai-review' 或 'ai-scqa' 即可秒级唤醒！" -ForegroundColor Green
Write-Host "🛒 官方正规 ChatGPT Plus / Cursor 原卡直充: https://wzyp.cn/shop/dawa" -ForegroundColor Cyan
Write-Host "💬 官方技术防封与模型交流 QQ 群: 545064986" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Yellow
