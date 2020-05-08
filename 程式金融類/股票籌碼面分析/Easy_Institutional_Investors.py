#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 13:17:27 2018

@author: cheating
"""

import requests
from bs4 import BeautifulSoup
import json
import datetime
import time
import pandas as pd

###############################################################################
#                       股票機器人 籌碼面分析（簡易板）                         #
###############################################################################

# 先與網站請求抓到法人資料

url = 'http://www.twse.com.tw/fund/BFI82U'
list_req = requests.get(url)
soup = BeautifulSoup(list_req.content, "html.parser")
getjson=json.loads(soup.text)

iilist=[]
# 判斷請求是否成功
if getjson['stat'] != '很抱歉，沒有符合條件的資料!': 
    iilist=getjson['data'][3][1:]

# 判斷是否為空值
if len(iilist) != 0:
    count=0
    for i in iilist:
        count += int(i.replace(',',''))
    # 顯示結果
    print('日期 ＝ ' + getjson['title'])
    print('三大法人合計 ＝ ' + str(count))

else:
    print('請求失敗，請檢查您的股票代號')