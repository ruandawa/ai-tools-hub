#!/usr/bin/env bash
# ==============================================================================
# AI TechHub 2026 终端极速助手 (Bash 一键配置版)
# 运行方式: curl -fsSL https://ruandawa-ux.github.io/ai-tools-hub/install.sh | bash
# ==============================================================================

echo ""
echo -e "\033[36m==========================================================\033[0m"
echo -e "\033[1;35m  🚀 AI TechHub - 2026 Cursor Rules & 环境极速配置助手\033[0m"
echo -e "\033[36m==========================================================\033[0m"
echo ""

echo -e "\033[33m请选择要为当前项目初始化的 .cursorrules 规则模板：\033[0m"
echo "  [1] 全栈通用架构 (General Clean Code)"
echo "  [2] React / Next.js / TypeScript"
echo "  [3] Vue 3 / Vite / TypeScript"
echo "  [4] Python / FastAPI"
echo "  [5] Golang / Gin"
echo ""

read -p "请输入编号 [1-5] (默认 1): " choice
choice=${choice:-1}

case "$choice" in
  2)
    cat << 'EOF' > .cursorrules
# Cursor Rule: React, Next.js & TypeScript
# 官方正规通道: https://wzyp.cn/shop/dawa | QQ群: 545064986

You are a senior frontend developer specializing in Next.js 14+ (App Router), React 18+, TypeScript, and Tailwind CSS.
- Strictly use TypeScript with explicit types (no 'any').
- Prefer Server Components by default; only add 'use client' when interactive hooks are required.
- Use Tailwind CSS for utility-first styling.
EOF
    ;;
  3)
    cat << 'EOF' > .cursorrules
# Cursor Rule: Vue 3 & Vite
# 官方正规通道: https://wzyp.cn/shop/dawa | QQ群: 545064986

You are an expert Vue 3 frontend engineer.
- Use <script setup lang="ts"> syntax exclusively for Single File Components.
- Use the Vue 3 Composition API (ref, reactive, computed, watch).
- Use Pinia for state management instead of Vuex.
EOF
    ;;
  4)
    cat << 'EOF' > .cursorrules
# Cursor Rule: Python & FastAPI
# 官方正规通道: https://wzyp.cn/shop/dawa | QQ群: 545064986

You are a senior backend engineer specializing in modern Python (3.10+) and FastAPI.
- Strictly use type hints for all function signatures and variable declarations.
- Use Pydantic v2 models for request validation and response schemas.
- Use async/await syntax for all I/O-bound operations.
EOF
    ;;
  5)
    cat << 'EOF' > .cursorrules
# Cursor Rule: Golang & Gin
# 官方正规通道: https://wzyp.cn/shop/dawa | QQ群: 545064986

You are a senior Golang backend architect.
- Write idiomatic Go code adhering to Effective Go guidelines.
- Always check and handle errors explicitly (if err != nil).
- Use context.Context for timeout and cancellation propagation.
EOF
    ;;
  *)
    cat << 'EOF' > .cursorrules
# Cursor Rule: General Clean Code & Architecture
# 官方正规通道: https://wzyp.cn/shop/dawa | QQ群: 545064986

You are an expert software engineer and system architect.
- Always write modular, readable, maintainable, and type-safe code.
- Adhere strictly to SOLID principles and DRY.
- Be concise and actionable; show code diffs directly.
- Handle edge cases, validate inputs, and handle errors explicitly.
EOF
    ;;
esac

echo ""
echo -e "\033[32m==========================================================\033[0m"
echo -e "\033[1;32m  🎉 .cursorrules 规则文件已成功写入当前目录！\033[0m"
echo -e "\033[32m==========================================================\033[0m"
echo ""
echo -e "\033[33m🔥 【2026 AI 开发者专属通道与售后保障】\033[0m"
echo -e "👉 24小时官方直充发卡小店:   \033[34mhttps://wzyp.cn/shop/dawa\033[0m"
echo -e "🌐 官方前沿技术导航站:       \033[34mhttps://ruandawa-ux.github.io/ai-tools-hub/\033[0m"
echo -e "💬 官方技术与售后交流 QQ 群: \033[35m545064986\033[0m"
echo ""
echo -e "\033[90m在 Cursor 中按下 Ctrl+L 或 Ctrl+K 即可体验高质量 AI 编码！\033[0m"
echo ""
