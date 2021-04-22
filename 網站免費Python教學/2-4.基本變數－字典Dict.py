# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 00:23:27 2021

@author: Ivan
內容來自：行銷搬進大程式
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第二章Python基本變數教學
基本變數－字典Dict
"""
# 一個key對應一個value
boxname = {
    'key1':'value1',
    'key2':'value2',
    'key3':'value3',
    'key4':{
        'key5':'value5',
        'key6':'value6'
        }
    }

#真正實際呈現的樣子
boxname2 = {
    '商品':'水壺',
    '容量(L)':2,
    '顏色':'草莓紅',
    '運費':{
        '台灣':65,
        '日本':70
        }
    }

#取資料
boxname2['容量(L)']
boxname2['運費']['台灣']

# 新增元素
boxname2['產品編號'] = 'N1938000029'

# 列印出所有元素
boxname2.items()

# 刪除元素
del boxname2['運費']

# 刪除元素，且回傳key
boxname2.pop('產品編號')
