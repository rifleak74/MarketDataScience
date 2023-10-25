# 載入LineBot所需要的套件
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app: Flask = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api: LineBotApi = LineBotApi('你自己的token')
# 必須放上自己的Channel Secret
handler: WebhookHandler = WebhookHandler('你自己的secret')

try:
    line_bot_api.push_message('你自己的ID', TextSendMessage(text='你可以開始了'))
except LineBotApiError as e:
    # 錯誤處理
    print(e.status_code)
    print(e.error.message)
    print(e.error.details)

@app.route("/callback", methods=['POST'])
def callback() -> str:
    """
    監聽所有來自 /callback 的 Post Request
    """
    # 取得 X-Line-Signature 標頭值
    signature: str = request.headers['X-Line-Signature']

    # 取得 request body 文字
    body: str = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # 處理 webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("無效的簽名。請檢查你的 channel access token/channel secret。")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event: MessageEvent):
    """
    訊息傳遞區塊
    基本上程式編輯都在這個function
    """
    try:
        message: TextSendMessage = TextSendMessage(text=event.message.text)
        line_bot_api.reply_message(event.reply_token,message)
    except LineBotApiError as e:
        # 錯誤處理
        print(e.status_code)
        print(e.error.message)
        print(e.error.details)

#主程式
import os
if __name__ == "__main__":
    port: int = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
