# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 09:34:52 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第一章 爬蟲基本訓練
Json爬蟲實戰－Google趨勢搜尋
"""
import requests
import json

 # 要抓取的網址
url = 'https://trends.google.com.tw/trends/api/dailytrends?hl=zh-TW&tz=-480&geo=TW&ns=15'
#請求網站
list_req = requests.get(url)
gettext = list_req.content
#將整個網站的程式碼爬下來
getdata = json.loads(gettext[6:])
