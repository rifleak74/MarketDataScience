# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 19:26:26 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第一章 爬蟲基本訓練
Json爬蟲實戰－PChome
"""
import requests
import json
import pandas as pd
import time

keyword = '鞋櫃'
# 要抓取的網址
url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q='+keyword+'&page=1&sort=sale/dc'
#請求網站
list_req = requests.get(url)
#將整個網站的程式碼爬下來
getdata = json.loads(list_req.content)


# 蒐集多頁的資料，打包成csv檔案
alldata = pd.DataFrame() # 準備一個容器
for i in range(1,10):
    # 要抓取的網址
    url = 'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q='+keyword+'&page='+str(i)+'&sort=sale/dc'
    #請求網站
    list_req = requests.get(url)
    #將整個網站的程式碼爬下來
    getdata = json.loads(list_req.content)
    todataFrame = pd.DataFrame(getdata['prods']) # 轉成Dataframe格式
    alldata = pd.concat([alldata, todataFrame]) # 將結果裝進容器
    
    time.sleep(5) #拖延時間
    
# 儲存檔案
alldata.to_csv('PChome.csv', # 名稱
               encoding='utf-8-sig', # 編碼 
               index=False) # 是否保留Index
