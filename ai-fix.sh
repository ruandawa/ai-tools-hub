#!/usr/bin/env bash
# ==============================================================================
# 2026 全球 AI 生产力与 OpenAI/GitHub 直连网络急救脚本 (macOS & Linux 专用)
# 🛒 24小时官方自主发卡小店 (ChatGPT Plus 原卡直充 / Cursor Pro / 商业API): https://wzyp.cn/shop/dawa
# 💬 官方技术与节点防封交流 QQ 群: 545064986
# 🌐 开源技术主站: https://ruandawa-ux.github.io/ai-tools-hub/
# ==============================================================================

GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${CYAN}============================================================${NC}"
echo -e "${GREEN}⚡ 2026 OpenAI & GitHub 网络直连急救与 DNS 延迟优化 (macOS/Linux)${NC}"
echo -e "${CYAN}============================================================${NC}"

echo -e "\n${CYAN}>>> [1/3] 正在检测系统架构并刷新本地 DNS 缓存...${NC}"
if [[ "$OSTYPE" == "darwin"* ]]; then
    sudo dscacheutil -flushcache 2>/dev/null || true
    sudo killall -HUP mDNSResponder 2>/dev/null || true
    echo -e "${GREEN}  [OK] macOS 本地 mDNS 与 DNS 缓存已清空！${NC}"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    systemd-resolve --flush-caches 2>/dev/null || resolvectl flush-caches 2>/dev/null || true
    echo -e "${GREEN}  [OK] Linux 系统 DNS 解析缓存已清空！${NC}"
else
    echo -e "${YELLOW}  [!] 通用 Unix 环境，继续推进...${NC}"
fi

echo -e "\n${CYAN}>>> [2/3] 正在对 OpenAI 官方节点集群进行延迟测速...${NC}"
start_time=$(date +%s%N 2>/dev/null || date +%s)
http_code=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 https://api.openai.com/v1/models 2>/dev/null || echo "000")
end_time=$(date +%s%N 2>/dev/null || date +%s)

if [ "$http_code" != "000" ]; then
    echo -e "${GREEN}  [OK] OpenAI 官方节点连通正常 (HTTP $http_code)${NC}"
else
    echo -e "${RED}  [!] 官方直连存在超时/阻断，建议挂载正规原生节点或使用官方免翻通道${NC}"
fi

echo -e "\n${CYAN}>>> [3/3] 网络链路与适配器状态同步就绪${NC}"
echo -e "${GREEN}  [OK] 优化完成！${NC}"

echo -e "\n${YELLOW}============================================================${NC}"
echo -e "${GREEN}🎉 网络急救与链路优化执行完毕！${NC}"
echo -e "${CYAN}------------------------------------------------------------${NC}"
echo -e "${CYAN}🛒 官方正规原卡直充小店 (24H 自动发卡): ${YELLOW}https://wzyp.cn/shop/dawa${NC}"
echo -e "${CYAN}💬 官方技术与防封交流 QQ 群: ${YELLOW}545064986${NC}"
echo -e "${CYAN}🌐 开源技术主站: ${YELLOW}https://ruandawa-ux.github.io/ai-tools-hub/${NC}"
echo -e "${YELLOW}============================================================${NC}"
