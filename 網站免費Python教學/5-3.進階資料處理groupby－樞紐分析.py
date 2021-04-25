# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:14:33 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第五章Pandas二維資料處理
進階資料處理groupby－樞紐分析
"""
import pandas as pd
#--- 匯入資料
salelist = pd.read_csv('salelist.csv') #也可使用read_excel
#--- groupby範例
salelist.groupby("product").mean()
# 計算每個商品quantity的平均
salelist[['product','quantity']].groupby("product").mean()

# 每筆訂單的總額
salelist['金額'] = salelist['quantity'] * salelist['price']
salelist[['tid','金額']].groupby("tid").mean()
