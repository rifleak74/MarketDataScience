#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 16:12:38 2018

@author: cheating
"""
import requests
from bs4 import BeautifulSoup
import json
import datetime
import time
import pandas as pd

###############################################################################
#                     股票機器人 標準差分析（簡易板）                         #
###############################################################################
# 抓到今天的時間
now = datetime.datetime.now()

# 先與網站請求抓到價格
def getstock(stocknumber='2002'):
    url = 'http://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20180814&stockNo=' + stocknumber + '&_=' + str(time.mktime(now.timetuple()))
    list_req = requests.get(url)
    soup = BeautifulSoup(list_req.content, "html.parser")
    getjson=json.loads(soup.text)
    
    # 判斷請求是否成功
    if getjson['stat'] != '很抱歉，沒有符合條件的資料!': 
        return [getjson['data']]
    else:
        return [] # 請求失敗回傳空值

# 開始計算股票的平均以及標準差
def Standard_Deviation(stocknumber='2002'):
    stocklist = getstock(stocknumber)
    
    # 判斷是否為空值
    if len(stocklist) != 0:
        stockdf = pd.DataFrame(stocklist[0],columns=["日期","成交股數","成交金額","開盤價","最高價","最低價","收盤價","漲跌價差","成交筆數"])
        stockAverage = pd.to_numeric(stockdf['收盤價']).mean()
        stockSTD = pd.to_numeric(stockdf['收盤價']).std()
        
        # 看看這隻股票現在是否便宜（平均-兩倍標準差）
        buy='很貴不要買'
        if pd.to_numeric(stockdf['收盤價'][-1:]).values[0] < stockAverage - (2*stockSTD):
            buy = '這隻股票現在很便宜喔！'
            
        # 顯示結果
        print('收盤價 ＝ ' + stockdf['收盤價'][-1:].values[0])
        print('\n中間價 ＝ ' + str(stockAverage))
        print('\n線距 ＝ ' + str(stockSTD))
        print(buy)
    else:
        print('請求失敗，請檢查您的股票代號')
       
Standard_Deviation(stocknumber='2002')