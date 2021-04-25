# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:25:07 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第五章Pandas二維資料處理
資料分類cut
"""
import pandas as pd
#--- 匯入資料
salelist = pd.read_csv('salelist.csv') #也可使用read_excel

# 把quantity欄位分成「少量購買」、「大量購買」
salelist['quantity_cut'] = pd.cut(salelist['quantity'], # 想分類的欄位
                               2, # 分成幾類
                               labels=["少量購買", "大量購買"] # 分類的名稱
                               ) 
# 自行決定切割間距
salelist['quantity_cut'] = pd.cut(salelist['quantity'], # 想分類的欄位
                               [0,2,6,17], # 分成幾類
                               labels=["少","中", "多"] # 分類的名稱
                               ) 