# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 16:01:36 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第一章 爬蟲基本訓練
Pandas爬蟲教學
"""
import pandas as pd

stock='2330'
 # 要抓取的網址
url = 'https://tw.stock.yahoo.com/q/q?s=' + stock 

getdata=pd.read_html(
    url, #想爬的網址
    encoding='big5', # 如何編碼爬下來的資料
    header=0, # 資料取代標題列
    )

getdata=pd.read_html(
    url, #想爬的網址
    encoding='big5', # 如何編碼爬下來的資料
    header=0, # 資料取代標題列
    attrs={'border':'2'}
    )
