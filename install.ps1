# ==============================================================================
# AI TechHub 2026 终端极速助手 (PowerShell 一键配置版)
# 运行方式: irm https://ruandawa-ux.github.io/ai-tools-hub/install.ps1 | iex
# ==============================================================================

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  🚀 AI TechHub - 2026 Cursor Rules & 环境极速配置助手" -ForegroundColor Magenta
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host ""

$templates = @{
    "1" = @{
        Name = "全栈通用架构规范 (General Clean Code)"
        Content = @"
# Cursor Rule: General Clean Code & Architecture
# 官方正规通道: https://wzyp.cn/shop/dawa | QQ群: 545064986

You are an expert software engineer and system architect.
- Always write modular, readable, maintainable, and type-safe code.
- Adhere strictly to SOLID principles and DRY.
- Be concise and actionable; show code diffs directly.
- Handle edge cases, validate inputs, and handle errors explicitly.
"@
    }
    "2" = @{
        Name = "React / Next.js / TypeScript 规范"
        Content = @"
# Cursor Rule: React, Next.js & TypeScript
# 官方正规通道: https://wzyp.cn/shop/dawa | QQ群: 545064986

You are a senior frontend developer specializing in Next.js 14+ (App Router), React 18+, TypeScript, and Tailwind CSS.
- Strictly use TypeScript with explicit types (no 'any').
- Prefer Server Components by default; only add 'use client' when interactive hooks are required.
- Use Tailwind CSS for utility-first styling.
"@
    }
    "3" = @{
        Name = "Vue 3 / Vite / TypeScript 规范"
        Content = @"
# Cursor Rule: Vue 3 & Vite
# 官方正规通道: https://wzyp.cn/shop/dawa | QQ群: 545064986

You are an expert Vue 3 frontend engineer.
- Use <script setup lang="ts"> syntax exclusively for Single File Components.
- Use the Vue 3 Composition API (ref, reactive, computed, watch).
- Use Pinia for state management instead of Vuex.
"@
    }
    "4" = @{
        Name = "Python / FastAPI 规范"
        Content = @"
# Cursor Rule: Python & FastAPI
# 官方正规通道: https://wzyp.cn/shop/dawa | QQ群: 545064986

You are a senior backend engineer specializing in modern Python (3.10+) and FastAPI.
- Strictly use type hints for all function signatures and variable declarations.
- Use Pydantic v2 models for request validation and response schemas.
- Use async/await syntax for all I/O-bound operations.
"@
    }
    "5" = @{
        Name = "Golang / Gin 规范"
        Content = @"
# Cursor Rule: Golang & Gin
# 官方正规通道: https://wzyp.cn/shop/dawa | QQ群: 545064986

You are a senior Golang backend architect.
- Write idiomatic Go code adhering to Effective Go guidelines.
- Always check and handle errors explicitly (if err != nil).
- Use context.Context for timeout and cancellation propagation.
"@
    }
}

Write-Host "请选择要为当前项目初始化的 .cursorrules 规则模板：" -ForegroundColor Yellow
Write-Host "  [1] 全栈通用架构 (General Clean Code)"
Write-Host "  [2] React / Next.js / TypeScript"
Write-Host "  [3] Vue 3 / Vite / TypeScript"
Write-Host "  [4] Python / FastAPI"
Write-Host "  [5] Golang / Gin"
Write-Host ""

$choice = Read-Host "请输入编号 [1-5] (直接回车默认 1)"
if ([string]::IsNullOrWhiteSpace($choice)) { $choice = "1" }
if (-not $templates.ContainsKey($choice)) { $choice = "1" }

$selected = $templates[$choice]
$targetPath = Join-Path (Get-Location) ".cursorrules"
Set-Content -Path $targetPath -Value $selected.Content -Encoding UTF8

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Green
Write-Host "  🎉 .cursorrules 规则文件已成功写入当前目录！" -ForegroundColor Green
Write-Host "==========================================================" -ForegroundColor Green
Write-Host ""
Write-Host "🔥 【2026 AI 开发者专属通道与售后保障】" -ForegroundColor Yellow
Write-Host "👉 24小时官方直充发卡小店:   https://wzyp.cn/shop/dawa" -ForegroundColor Cyan
Write-Host "🌐 官方前沿技术导航站:       https://ruandawa-ux.github.io/ai-tools-hub/" -ForegroundColor Cyan
Write-Host "💬 官方技术与售后交流 QQ 群: 545064986" -ForegroundColor Magenta
Write-Host ""
Write-Host "在 Cursor 中按下 Ctrl+L 或 Ctrl+K 即可体验高质量 AI 编码！" -ForegroundColor Gray
Write-Host ""
