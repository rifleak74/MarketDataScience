# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 09:38:35 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第一章 爬蟲基本訓練
Pandas爬蟲實戰－氣象預報
"""
import pandas as pd
import requests
import json
import datetime
from dateutil.relativedelta import relativedelta
import time
import random
import tqdm

# 爬取網站：http://tianqi.2345.com/
areaId = '71294' # 台北
areaType = '2'
year = '2021'
month = '3'
# 要抓取的網址
url = 'http://tianqi.2345.com/Pc/GetHistory?areaInfo%5BareaId%5D='+ str(areaId) +'&areaInfo%5BareaType%5D='+ str(areaType) +'&date%5Byear%5D='+ str(year) +'&date%5Bmonth%5D='+ str(month)
#請求網站
list_req = requests.get(url)
#將整個網站的程式碼爬下來
getJson = json.loads(list_req.content)
getTable = pd.read_html(getJson['data'],header = 0)
getTable[0] # 抓到資料


#--- 取得大量資料，該地區12個月
today = datetime.datetime.today()

areaId = '71294' # 台北
areaType = '2'
containar = pd.DataFrame() # 準備一個容器
for i in tqdm.tqdm(range(12)):
    countDay = today - relativedelta(months=i)
    year = countDay.year
    month = countDay.month
    # 要抓取的網址
    url = 'http://tianqi.2345.com/Pc/GetHistory?areaInfo%5BareaId%5D='+ str(areaId) +'&areaInfo%5BareaType%5D='+ str(areaType) +'&date%5Byear%5D='+ str(year) +'&date%5Bmonth%5D='+ str(month)
    
    #請求網站
    print(str(i)+'開始請求')
    list_req = requests.get(url)
    print(str(i)+'請求完成')
    #將整個網站的程式碼爬下來
    getJson = json.loads(list_req.content)
    getTable = pd.read_html(getJson['data'],header = 0)
    # 合併資料
    containar = pd.concat([containar, getTable[0]])
    
    # 休息一下
    time.sleep(random.randint(45,70))
    
containar.to_csv('台北天氣情況.csv',
                 encoding = 'utf-8-sig',
                 index = False
                 )