# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 10:34:15 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第一章 爬蟲基本訓練
Html爬蟲Post教學－台灣股市資訊網
"""
import requests
from bs4 import BeautifulSoup

# 要抓取的網址
url = 'https://goodinfo.tw/StockInfo/StockDividendPolicy.asp?STOCK_ID=2002'
# 附帶的資料必須要有
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36' }

#請求網站
list_req = requests.post(url, headers=headers)
#將整個網站的程式碼爬下來
soup = BeautifulSoup(list_req.content, "html.parser")
#抓取想要的資料
soup.find('td',{'style':'color:red'}).text
