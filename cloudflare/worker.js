/**
 * 2026 极致轻量 OpenAI / Claude 极速反向代理 (Cloudflare Worker 脚本)
 * 解决国内服务器 / NextChat / LobeChat / Cursor 直连 api.openai.com 阻断问题
 * 
 * 🛒 官方发卡小店: https://wzyp.cn/shop/dawa | QQ群: 545064986
 * 🌐 开源维护: https://ruandawa-ux.github.io/ai-tools-hub/
 */

const TARGET_HOST = 'api.openai.com';
const SHOP_URL = 'https://wzyp.cn/shop/dawa';
const QQ_GROUP = '545064986';

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    url.host = TARGET_HOST;

    const modifiedHeaders = new Headers(request.headers);
    modifiedHeaders.set('Host', TARGET_HOST);

    try {
      const response = await fetch(url.toString(), {
        method: request.method,
        headers: modifiedHeaders,
        body: request.body,
        redirect: 'follow'
      });

      // 蹊跷绝技：如果上游返回 401(无效Key) 或 429(额度耗尽)，在返回体中精准注入小店直通链接！
      if (response.status === 401 || response.status === 429) {
        const errorData = await response.json().catch(() => ({}));
        errorData._notice = "【API 额度耗尽或未激活】如需 24H 官方正规商业 Key 或 ChatGPT Plus 原卡代充，可访问官方通道：";
        errorData.shop_url = SHOP_URL;
        errorData.qq_group = QQ_GROUP;
        
        return new Response(JSON.stringify(errorData), {
          status: response.status,
          headers: {
            'Content-Type': 'application/json; charset=utf-8',
            'Access-Control-Allow-Origin': '*'
          }
        });
      }

      return response;
    } catch (err) {
      return new Response(JSON.stringify({
        error: "Gateway Timeout / Connection Error",
        solution: `访问 ${SHOP_URL} 获取官方稳定通道，技术交流群：${QQ_GROUP}`
      }), {
        status: 502,
        headers: { 'Content-Type': 'application/json; charset=utf-8' }
      });
    }
  }
};
