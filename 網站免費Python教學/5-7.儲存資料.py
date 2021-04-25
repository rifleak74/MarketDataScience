# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:29:03 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第五章Pandas二維資料處理
儲存資料
"""
import pandas as pd
#--- 製造資料
data = {'uid':[1,2,3,4,5,6,7],
        'name':['Jacky','Lily','Kevin',
                'Bob','Harry','Bill','Harry'],
        'age':[21,21,35,18,15,49,7]}
member = pd.DataFrame(data)

# 也可使用to_excel
member.to_csv('檔案名稱1.csv', # 檔案名稱
                encoding = 'utf-8-sig', # 編碼
                index=False # 是否保留index
                )