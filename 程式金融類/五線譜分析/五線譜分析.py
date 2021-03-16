# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 18:30:28 2021

@author: Ivan
五線譜分析概念修改自薛兆亨教授
"""

import twstock
import pandas as pd
from pandas_datareader import data
import datetime
from tqdm import tqdm 

allstock = pd.DataFrame( twstock.codes).T #取得全台股號
# 篩選想要的股票，只留下上市上櫃
allstock = allstock[allstock[0] != '特別股']
allstock = allstock[allstock[0] != '上櫃認購(售)權證']
allstock = allstock[allstock[0] != '上市認購(售)權證']
allstock = allstock[allstock[0] != '臺灣存託憑證(TDR)']
allstock = allstock[allstock[0] != '受益證券-不動產投資信託']
allstock = allstock[allstock[0] != '受益證券-資產基礎證券']
allstock = allstock[allstock[0] != 'ETF']

# 製作代號欄位
allstock[5] = allstock[5].replace('上櫃', 'TWO')
allstock[5] = allstock[5].replace('上市', 'TW')
allstock[8] = allstock[1] + '.' +allstock[5]

#先設定要爬的時間
start = datetime.datetime.now() - datetime.timedelta(days=1095) 
end = datetime.date.today()

candidate = []
Broken = []
for stock in tqdm(allstock[8]): # 每筆資料開始進行爬取
    try:
        df_stock = data.DataReader(stock, 'yahoo', start, end)
    except:
        Broken.append(stock) # 壞掉的股票也做紀錄
    theSTD = df_stock['Open'].std()
    theMean = df_stock['Open'].mean()
    last_price = df_stock['Open'][-1]
    if last_price < 100: # 超過100，太貴了
        if last_price < theMean - theSTD*2: #找到低於兩倍標準差的股票
            candidate.append(stock)