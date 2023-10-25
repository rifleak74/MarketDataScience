# 使用官方 Python 基礎映像
FROM python:3.11.5-slim

# 設定工作目錄
WORKDIR /app

# 將當前目錄的內容複製到工作目錄中
COPY . /app

# 安裝所需的套件
RUN pip install --no-cache-dir -r requirements.txt

# 讓外部連線可以存取到 Flask 應用程式
EXPOSE 5000

# 啟動 Flask 應用程式
CMD ["python", "app.py"]
