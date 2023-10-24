# telegramBot

這是一個使用 Flask 和 Telegram API 建立的機器人應用程式。

## 專案結構

```
.
├── Dockerfile
├── docker-compose.yml
└── app.py
```

## 檔案說明

- `app.py`：這是主要的應用程式檔案，包含了 Flask 應用程式的初始化和路由設定，以及 Telegram 機器人的設定和訊息處理。
- `Dockerfile`：這個檔案定義了 Docker 映像的建立過程，包括基礎映像的選擇、工作目錄的設定、應用程式檔案的複製、套件的安裝和應用程式的啟動。
- `docker-compose.yml`：這個檔案定義了 Docker 容器的配置，包括映像的建立、端口的映射和環境變數的設定。

## 使用說明

1. 先確保你的電腦已經安裝了 Docker 和 Docker Compose。
2. 將你的 Telegram 機器人 token 填入 `app.py` 中的對應位置。
3. 在專案根目錄下執行 `docker-compose up` 命令來啟動應用程式。
4. 你的應用程式現在應該已經在 http://localhost:5000/ 運行了。

## 注意事項

- 如果你在本地運行應用程式，請確保 5000 端口沒有被其他應用程式佔用。
- 請確保你的 Telegram 機器人 token 是正確的，否則機器人將無法正常工作。

## 開發環境

- Python 3.11.5
- Flask
- Telegram API
