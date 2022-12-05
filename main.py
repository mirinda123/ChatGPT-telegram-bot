from revChatGPT.revChatGPT import Chatbot
import json
import logging
import os
import textwrap
from telegram import Update
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler


def get_input(prompt):
    # prompt for input
    lines = []
    print(prompt, end="")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    # Join the lines, separated by newlines, and print the result
    user_input = "\n".join(lines)
    # print(user_input)
    return user_input


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="欢迎使用ChatGPT")


async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatbot.reset_chat()
    await context.bot.send_message(chat_id=update.effective_chat.id, text="已重置对话上下文")

async def refresh(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatbot.refresh_session()
    # Save the new config
    with open("config.json", "w") as f:
        json.dump(chatbot.config, f)
    await context.bot.send_message(chat_id=update.effective_chat.id, text="已刷新新的会话")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lines_printed = 0
    result = ""
    try:
        print("Chatbot: ")
        formatted_parts = []
        for message in chatbot.get_chat_response(update.message.text, output="stream"):
            # Split the message by newlines
            message_parts = message['message'].split('\n')

            # Wrap each part separately
            formatted_parts = []
            for part in message_parts:
                formatted_parts.extend(textwrap.wrap(part, width=80))
                for formatted_line in formatted_parts:
                    if len(formatted_parts) > lines_printed + 1:
                        # print(formatted_parts[lines_printed])
                        result += formatted_parts[lines_printed]
                        lines_printed += 1
        # print(formatted_parts[lines_printed])
        result += formatted_parts[lines_printed]
    except Exception as e:
        print("Something went wrong!")
        print(e)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=result)


if __name__ == "__main__":

    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    with open("config.json", "r") as f:
        config = json.load(f)
    chatbot = Chatbot(config)
    if 'session_token' in config:
        chatbot.refresh_session()
    if 'http_proxy' in config and config['http_proxy'] != "":
        os.environ["http_proxy"] = config['http_proxy']
    if 'https_proxy' in config and config['https_proxy'] != "":
        os.environ["https_proxy"] = config['https_proxy']

    application = ApplicationBuilder().token('<your_token>').build()
    start_handler = CommandHandler('start', start)
    reset_handler = CommandHandler('reset', reset)
    refresh_handler = CommandHandler('refresh', refresh)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(reset_handler)
    application.add_handler(refresh_handler)
    application.add_handler(echo_handler)

    application.run_polling()
