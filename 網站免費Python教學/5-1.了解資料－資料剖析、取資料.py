# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 19:37:40 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第五章Pandas二維資料處理
了解資料－資料剖析、取資料
"""
import pandas as pd
#--- 製造資料
data = {'顧客編號':[1,2,3,4,5,6,7],
        '姓名':['Jacky','Lily','Kevin',
                'Bob','Harry','Bill','Harry'],
        '年齡':[21,21,35,18,15,49,7]}
member = pd.DataFrame(data)

#--- 資料剖析
member.head() # 列出前五筆資料
member.info() # 資料資訊
member.shape # (列數，欗數)
member.columns #列出所有欄位
member.index #列出所有列

#--- 取欄位資料
member['年齡'] #取出某欄位
# 取出 uid 與age 欄位
member[['顧客編號','姓名']]

# 只顯示'姓名' 為 Harry 的交易數據
member[member['姓名'] == 'Harry'] 

step1 = member['姓名'] == 'Harry'
step2 = member['年齡'] < 10
member[(step1 & step2)] 

#--- 了解個別欄位資料
member['年齡'].max() #最大值
member['年齡'].min() #最小值
member['年齡'].mean() #平均值
member['年齡'].std() #標準差
member['年齡'].count() #總數量
member['年齡'].describe() #欄位資訊

member['姓名'].value_counts() #計算個數並依大到小排序
member['年齡'].sum() # 加總