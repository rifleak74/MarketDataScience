# -*- coding: utf-8 -*-
"""
Created on Tue May 11 13:48:24 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第一章 爬蟲基本訓練
氣象預報圖像化
"""
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np

getdata = pd.read_csv('台北天氣情況.csv', encoding = 'utf-8')
getdata.columns
getdata['最高温'] = getdata['最高温'].str[:-1].astype(int)
getdata['最低温'] = getdata['最低温'].str[:-1].astype(int)
getdata['是否下雨'] = np.where(getdata['天气'].str.contains('雨'),1,0)

getdata['日期'] = pd.to_datetime(getdata['日期'].str[:-3])
getdata.sort_values(by=['日期'], inplace = True)
getdata['日期'] = getdata['日期'].astype(str).str[:-3]
rain = getdata.groupby(
            '日期',
            as_index = False # 分類條件是否要取代Index
            )['是否下雨'].sum()

highC = getdata.groupby(
            '日期',
            as_index = False # 分類條件是否要取代Index
            )['最高温'].max()

lowC = getdata.groupby(
            '日期',
            as_index = False # 分類條件是否要取代Index
            )['最低温'].min()
# 棒狀圖
names = rain['日期']
plt.bar(names, # X資料
        highC['最高温'], # Y資料
        0.5, # bar寬度
        color='#EF798A' # bar顏色
        )
plt.bar(names, # X資料
        lowC['最低温'], # Y資料
        0.5, # bar寬度
        color='#7CA5B8' # bar顏色
        )
plt.plot(names,
    rain['是否下雨'],
    color='#000000'
    )
plt.title('天氣狀況－台北地區', fontsize = 30) #加入標題
plt.xlabel('時間') #加x軸標籤
plt.ylabel('溫度') #加y軸標籤
plt.xticks(rotation=30)
plt.show()
