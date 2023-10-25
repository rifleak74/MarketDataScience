# Line Bot Python 程式碼

這是一個使用 Python 和 Flask 框架，以及 Line Messaging API 來建立 Line Bot 的範例程式碼。

## 環境設定

首先，你需要在你的 LINE Developers 控制台中建立一個新的 Messaging API 服務，並取得 Channel Access Token 和 Channel Secret。

然後，將這些資訊填入程式碼中對應的位置：

```python
# 必須放上自己的Channel Access Token
line_bot_api: LineBotApi = LineBotApi('你自己的token')
# 必須放上自己的Channel Secret
handler: WebhookHandler = WebhookHandler('你自己的secret')
```

## 執行程式碼

你可以在本地或者伺服器上執行這個程式碼。如果你在本地運行，你可能需要使用 ngrok 或其他類似的工具來建立一個公開的網址，以便 Line 服務能夠訪問你的 webhook。

## 錯誤處理

這個程式碼包含了基本的錯誤處理。如果在處理 Line 事件或發送訊息時出現錯誤，程式碼會捕獲這個錯誤並打印出錯誤的詳細信息。

## 進一步學習

如果你想要進一步學習如何使用 Line Messaging API，你可以參考 [LINE Messaging API SDK for Python](https://github.com/line/line-bot-sdk-python) 的官方文件。
