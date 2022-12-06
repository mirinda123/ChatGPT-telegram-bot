# ChatGPT-telegram-bot
快速轻量级搭建电报ChatGPT机器人，使用[@acheong08](https://github.com/acheong08)中使用的API，无需模拟浏览器

# ChatGPT 注册方法

[OpenAI 推出超神 ChatGPT 注册攻略来了](https://www.v2ex.com/t/900126#reply145)

# 安装

```
pip install revChatGPT --upgrade
pip install python-telegram-bot --upgrade --pre
```

# 使用方法



在`config.json`文件中填写代理服务器地址（可选），同时必须填写电报bot的token，接着`python main.py` 启动服务器。

在`telegram`中登录。有两种登录方式：

1. `/login <username> <password>`，通过用户名和密码进行登录
2. `/token <session_token>`，通过token的方式登录，获得`session_token`的方法见[这里](https://github.com/acheong08/ChatGPT)

接着对bot发送文字即可

还支持：

`/reset`：忘掉之前的对话，重新开始新的对话

`/refresh`：刷新网页，重新获得一个`session_token`

