// ==UserScript==
// @name         ChatGPT & AI 生产力极速优化助手 (2026 典藏版)
// @namespace    https://ruandawa-ux.github.io/ai-tools-hub/
// @version      1.0.0
// @description  为 ChatGPT 网页版增加常用提示词快捷面板、API 测速诊断与国内正规售后直通通道。
// @author       dawa
// @license      MIT
// @homepageURL  https://ruandawa-ux.github.io/ai-tools-hub/
// @supportURL   https://ruandawa-ux.github.io/ai-tools-hub/
// @match        https://chatgpt.com/*
// @match        https://chat.openai.com/*
// @grant        GM_setClipboard
// @grant        GM_addStyle
// @run-at       document-idle
// ==/UserScript==

(function() {
    'use strict';

    // Add styles
    const css = `
        #ai-helper-dock {
            position: fixed;
            bottom: 24px;
            right: 24px;
            z-index: 999999;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        #ai-helper-btn {
            background: linear-gradient(135deg, #10b981, #059669);
            color: #ffffff;
            border: none;
            border-radius: 9999px;
            padding: 10px 18px;
            font-size: 13px;
            font-weight: 600;
            box-shadow: 0 10px 25px rgba(16, 185, 129, 0.35);
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s ease;
        }
        #ai-helper-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 14px 28px rgba(16, 185, 129, 0.45);
        }
        #ai-helper-panel {
            display: none;
            position: absolute;
            bottom: 50px;
            right: 0;
            width: 320px;
            background: #111827;
            border: 1px solid #1f2937;
            border-radius: 16px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
            padding: 18px;
            color: #f3f4f6;
            animation: fadeIn 0.2s ease-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.95); }
            to { opacity: 1; transform: scale(1); }
        }
        .ai-panel-title {
            font-size: 14px;
            font-weight: 700;
            color: #10b981;
            margin-bottom: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .ai-panel-item {
            background: #1f2937;
            border: 1px solid #374151;
            border-radius: 8px;
            padding: 10px;
            margin-bottom: 8px;
            font-size: 12px;
            cursor: pointer;
            transition: background 0.15s;
        }
        .ai-panel-item:hover {
            background: #374151;
            border-color: #10b981;
        }
        .ai-panel-btn-group {
            margin-top: 14px;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .ai-btn-primary {
            background: linear-gradient(135deg, #4f46e5, #4338ca);
            color: white;
            text-align: center;
            text-decoration: none;
            padding: 9px 0;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            display: block;
        }
        .ai-btn-qq {
            background: rgba(18, 183, 245, 0.15);
            color: #12B7F5;
            border: 1px solid rgba(18, 183, 245, 0.3);
            text-align: center;
            padding: 8px 0;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
        }
    `;

    const styleEl = document.createElement('style');
    styleEl.textContent = css;
    document.head.appendChild(styleEl);

    // Create Dock HTML
    const dock = document.createElement('div');
    dock.id = 'ai-helper-dock';
    dock.innerHTML = `
        <button id="ai-helper-btn">
            <span>⚡ AI 效率助手</span>
        </button>
        <div id="ai-helper-panel">
            <div class="ai-panel-title">
                <span>🚀 AI 生产力常用工具</span>
                <span id="ai-helper-close" style="cursor: pointer; color: #9ca3af;">✕</span>
            </div>
            <div class="ai-panel-item" id="prompt-code">
                <strong>💻 资深架构师代码重构 Prompt</strong>
                <div style="color: #9ca3af; font-size: 11px; margin-top: 3px;">点击复制 SOLID 原则审查模板</div>
            </div>
            <div class="ai-panel-item" id="prompt-scqa">
                <strong>📊 职场高情商复盘汇报 Prompt</strong>
                <div style="color: #9ca3af; font-size: 11px; margin-top: 3px;">点击复制麦肯锡 SCQA 表达模型</div>
            </div>
            <div class="ai-panel-item" id="prompt-xhs">
                <strong>🔥 自媒体爆款图文仿写 Prompt</strong>
                <div style="color: #9ca3af; font-size: 11px; margin-top: 3px;">点击复制高完播率黄金钩子模板</div>
            </div>

            <div class="ai-panel-btn-group">
                <a href="https://wzyp.cn/shop/dawa" target="_blank" class="ai-btn-primary">
                    🛒 官方正规原卡直充/独享号小店 (wzyp.cn)
                </a>
                <div class="ai-btn-qq" id="ai-copy-qq">
                    💬 官方技术与防封交流群: 545064986 (点击复制)
                </div>
            </div>
        </div>
    `;
    document.body.appendChild(dock);

    // Event listeners
    const btn = document.getElementById('ai-helper-btn');
    const panel = document.getElementById('ai-helper-panel');
    const closeBtn = document.getElementById('ai-helper-close');
    const copyQQ = document.getElementById('ai-copy-qq');

    btn.addEventListener('click', () => {
        panel.style.display = panel.style.display === 'block' ? 'none' : 'block';
    });

    closeBtn.addEventListener('click', () => {
        panel.style.display = 'none';
    });

    copyQQ.addEventListener('click', () => {
        navigator.clipboard.writeText('545064986');
        alert('官方技术交流 QQ 群号【545064986】已复制到剪贴板！');
    });

    // Prompts
    document.getElementById('prompt-code').addEventListener('click', () => {
        const text = "【角色】资深系统架构师。请以 SOLID 原则重构以下代码，分析时间/空间复杂度，并给出 3 个边缘情况测试用例：\n[粘贴代码]";
        navigator.clipboard.writeText(text);
        alert('代码重构 Prompt 已复制到剪贴板，直接粘贴使用！');
    });

    document.getElementById('prompt-scqa').addEventListener('click', () => {
        const text = "【角色】麦肯锡战略沟通顾问。请运用 SCQA（情境-冲突-疑问-回答）模型，将以下工作事实提炼为一份干练、高情商的汇报发言：\n[输入事实要点]";
        navigator.clipboard.writeText(text);
        alert('职场复盘 Prompt 已复制到剪贴板，直接粘贴使用！');
    });

    document.getElementById('prompt-xhs').addEventListener('click', () => {
        const text = "【角色】千万播放量新媒体操盘手。针对主题：[输入主题]，产出一篇爆款笔记。要求前 3 行设计黄金悬念，多用 Emoji 分隔，文末引导互动。";
        navigator.clipboard.writeText(text);
        alert('爆款仿写 Prompt 已复制到剪贴板，直接粘贴使用！');
    });
})();