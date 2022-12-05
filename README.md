# ChatGPT-telegram-bot
快速轻量级搭建电报ChatGPT机器人，无需模拟浏览器，使用[@acheong08](https://github.com/acheong08)中使用的API

# ChatGPT 注册方法

[OpenAI 推出超神 ChatGPT 注册攻略来了](https://www.v2ex.com/t/900126#reply145)

# 安装

```
pip3 install revChatGPT --upgrade
pip install python-telegram-bot --upgrade --pre
```

# 使用方法

在`config.json`文件中填写`session_token`，bot的`token`，然后`python main.py`，对bot发送文字即可

`/reset`：忘掉之前的对话，重新开始新的对话

`/refresh`：刷新网页，重新获得一个`session_token`

