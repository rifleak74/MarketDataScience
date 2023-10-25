import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, MessageHandler, Filters, CallbackContext

# 初始化 Flask 應用
app: Flask = Flask(__name__)

# 設定你的 token
bot: Bot = Bot(token='你的 token')

@app.route('/hook', methods=['POST'])
def webhook_handler() -> str:
    """
    當路由 /hook 使用 POST 方法時，將觸發此方法。

    Returns:
        str: 回傳 'ok' 字串
    """
    if request.method == "POST":
        update: Update = Update.de_json(request.get_json(force=True), bot)

        # 更新調度器處理程序以處理此訊息
        dispatcher.process_update(update)
    return 'ok'


def reply_handler(update: Update, _: CallbackContext) -> None:
    """
    回覆處理程序。

    Args:
        update (Update): 從使用者接收到的更新訊息
        _ (CallbackContext): 回呼上下文，此處不使用，所以命名為 "_"
    """
    user = update.message.from_user
    user_text = update.message.text
    update.message.reply_text(user_text)

# 為機器人新建一個調度器
dispatcher: Dispatcher = Dispatcher(bot, None, use_context=True)

# 為調度器添加處理程序，處理各種類型的訊息。此處的處理程序專門處理文字訊息。
dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))

if __name__ == "__main__":
    # 運行伺服器
    port: int = int(os.environ.get('PORT', 27017))
    app.run(host='0.0.0.0', port=port)
