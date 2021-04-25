# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 23:23:28 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第五章Pandas二維資料處理
合併資料－concat、merge
"""
import pandas as pd
#--- 匯入資料
salelist = pd.read_csv('salelist.csv') #也可使用read_excel
#--- 製造資料
data = {'uid':[1,2,3,4,5,6,7],
        'name':['Jacky','Lily','Kevin',
                'Bob','Harry','Bill','Harry'],
        'age':[21,21,35,18,15,49,7]}
member = pd.DataFrame(data)


#--- concat範例
pd.concat([member, salelist], axis=0)

#--- merga範例
member.merge(salelist, #想合併的資料表
             on = 'uid', # 主鍵
             how = 'left' # 怎麼合併 left, right, outer, inner
             )