# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 12:39:41 2019

@author: Ivan
"""
from fugle_realtime import intraday
import schedule
import time

def stockPrice_check(stock, check_price):
    stockdf=intraday.trades(apiToken="你的Token", 
                output="dataframe", 
                symbolId=stock)
    nowprice = stockdf['price'].values[-1]
    if nowprice > check_price:
        print(stock + ' 目前價格 ' + str(nowprice))
        
def job():
    allstock = ['2330','2002','1101']
    allprice = [310, 28 , 41]
    for i,j in zip(allstock, allprice):
        stockPrice_check(i, j)
   

second_5_j = schedule.every(3).seconds.do(job)


# 無窮迴圈
while True: 
    schedule.run_pending()
    time.sleep(1)

# 列出工作目錄
#schedule.jobs

# 清除工作目錄
#schedule.clear()