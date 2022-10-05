import os
import telegram
from flask import Flask, request
from telegram.ext import Dispatcher, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Bot, Update, KeyboardButton, ReplyKeyboardMarkup

# Initial Flask app
app = Flask(__name__)

# 設定你的token
bot = telegram.Bot(token=('你的token'))
bot.send_message(chat_id = '你的ID', text ='你可以開始了')

@app.route('/hook', methods=['POST'])
def webhook_handler():
    """Set route /hook with POST method will trigger this method."""
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        # Update dispatcher process that handler to process this message
        dispatcher.process_update(update)
    return 'ok'


def reply_handler(update: Update, _: CallbackContext):
    """自動回復"""
    user = update.message.from_user
    userText = update.message.text
    update.message.reply_text(userText)

# New a dispatcher for bot
dispatcher = Dispatcher(bot, None)

# Add handler for handling message, there are many kinds of message. For this handler, it particular handle text
# message.
dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))

if __name__ == "__main__":
    # Running server
    port = int(os.environ.get('PORT', 27017))
    app.run(host='0.0.0.0', port=port)
