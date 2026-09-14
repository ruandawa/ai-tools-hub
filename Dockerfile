FROM nginx:alpine
LABEL maintainer="dawa <dawa@wzyp.cn>"
LABEL description="2026 AI Tools Hub & OpenAI ChatGPT Plus Navigation"

COPY ./index.html /usr/share/nginx/html/index.html
COPY ./install.ps1 /usr/share/nginx/html/install.ps1
COPY ./install.sh /usr/share/nginx/html/install.sh
COPY ./chatgpt-helper.user.js /usr/share/nginx/html/chatgpt-helper.user.js

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]