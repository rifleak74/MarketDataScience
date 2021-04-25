# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:11:53 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第五章Pandas二維資料處理
基本資料處理－匯入、排序、刪除、取代、型態轉換
"""
import pandas as pd
#--- 匯入資料
salelist = pd.read_csv('salelist.csv') #也可使用read_excel

# 排序(遞減)
salelist['quantity'].sort_values(ascending=False) # False=遞減， True=遞增

# 資料+-*/
salelist['quantity'] * salelist['price']

# 移除 uid 與 age
salelist.drop(columns=['tid','uid']) 

#--- 資料型態轉換
salelist['price'] = salelist['price'].astype('float64') #int, str
salelist.values # 轉換回array
salelist.values.tolist() # 轉換回list

#--- 更換columns名稱
salelist.columns = ['資料編號','交易序號','交易日期','顧客編號','產品','數量','價格']

#--- 取代部分資料內容，比較兩者差別
salelist['產品'].str.replace('an','@') 
salelist['產品'].replace('an','@') 
