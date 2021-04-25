# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:26:16 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第五章Pandas二維資料處理
時間欄位處理
"""
import pandas as pd
#--- 匯入資料
salelist = pd.read_csv('salelist.csv') #也可使用read_excel\

# pd.to_datetime(salelist['date']) # 民國資料無法直接轉換
getdate = salelist['date'].str[0:3] # 取出欄位「交易日期」的前三個字元
getdate = getdate.astype('int') # 型態轉換
getdate = getdate + 1911 # 換成西元
salelist['(新)交易日期'] = getdate.astype(str) + salelist['date'].str[3:]
pd.to_datetime(salelist['(新)交易日期'], # 欲轉換資料
               format='%Y-%m-%d') # 轉換前的格式