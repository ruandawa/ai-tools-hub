@echo off
chcp 65001 >nul
title 2026 OpenAI 与 GitHub 网络急救加速工具
echo ============================================================
echo  2026 OpenAI 与 GitHub 网络直连急救与 DNS 延迟优化工具
echo  🛒 官方直充小店: https://wzyp.cn/shop/dawa ^| QQ群: 545064986
echo ============================================================
echo.

>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if '%errorlevel%' NEQ '0' (
    echo [提示] 正在请求管理员权限...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
    pushd "%CD%"
    CD /D "%~dp0"

echo [1/3] 正在清空并刷新系统 DNS 缓存...
ipconfig /flushdns >nul
echo [OK] 本地 DNS 缓存已清空！
echo.

echo [2/3] 正在备份并更新系统 Hosts 映射...
copy /y "%SystemRoot%\System32\drivers\etc\hosts" "%SystemRoot%\System32\drivers\etc\hosts.bak" >nul

echo. >> "%SystemRoot%\System32\drivers\etc\hosts"
echo # 2026 AI TechHub 加速配置 - wzyp.cn/shop/dawa >> "%SystemRoot%\System32\drivers\etc\hosts"
echo 140.82.113.4      github.com >> "%SystemRoot%\System32\drivers\etc\hosts"
echo 185.199.108.133   raw.githubusercontent.com >> "%SystemRoot%\System32\drivers\etc\hosts"
echo 104.18.2.161      api.openai.com >> "%SystemRoot%\System32\drivers\etc\hosts"
echo 104.18.32.47      chatgpt.com >> "%SystemRoot%\System32\drivers\etc\hosts"
echo [OK] Hosts 干净 IP 注入完成！
echo.

echo [3/3] 重新激活网络适配器...
ipconfig /flushdns >nul
echo [OK] 直连优化已全部生效！
echo.

echo ============================================================
echo 🎉 网络急救优化成功！
echo ------------------------------------------------------------
echo 🛒 官方正规原卡直充小店 (24H 自动发卡): https://wzyp.cn/shop/dawa
echo 💬 官方技术与节点防封交流 QQ 群: 545064986
echo 🌐 开源技术主站: https://ruandawa-ux.github.io/ai-tools-hub/
echo ============================================================
pause
