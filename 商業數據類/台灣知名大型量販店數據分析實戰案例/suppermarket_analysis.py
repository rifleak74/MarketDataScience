#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 09:34:58 2020

@author: ivan
"""
import pandas as pd
import platform
from matplotlib.font_manager import FontProperties
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

# 判斷是甚麼作業系統
theOS = list(platform.uname())[0]
if theOS == 'Windows':
    theOS = '\\'
    ecode = 'utf-8-sig'
else:
    theOS = '/'
    ecode = 'utf-8'
    
#讀取檔案
data = pd.read_csv('商業數據分析-實作3：商店24小時來客資料.csv',encoding = ecode)

#--- 來客數的視覺化
plt.plot(data['時間'], data[' 平日來客數 '], '-o',label='平日來客數') #給予線標籤
plt.plot(data['時間'], data[' 週末來客數 '], '-o', label='週末來客數') #給予線標籤
plt.xticks(fontsize=15,rotation=90)
plt.grid(True) # grid 開啟
plt.xlabel('時間（0-24點）',fontsize=15)
plt.ylabel('來客數',fontsize=15)
plt.title('來客數的視覺化',fontsize=30)
plt.legend(bbox_to_anchor=(1.03, 0.8), loc=2) #開啟圖例
plt.show()



#--- 客單價的視覺化
data['平日客單價']  = data[' 平日營業額'] / data[' 平日來客數 ']
data['週末客單價']  = data[' 週末營業額'] / data[' 週末來客數 ']
plt.plot(data['時間'], data['平日客單價'], '-o',label='平日客單價') #給予線標籤
plt.plot(data['時間'], data['週末客單價'], '-o', label='週末客單價') #給予線標籤
plt.xticks(fontsize=15,rotation=90)
plt.grid(True) # grid 開啟
plt.xlabel('時間（0-24點）',fontsize=15)
plt.ylabel('客單價',fontsize=15)
plt.title('客單價的視覺化',fontsize=30)
plt.legend(bbox_to_anchor=(1.03, 0.8), loc=2) #開啟圖例
plt.show()



#--- 營業額的視覺化
plt.plot(data['時間'], data[' 平日營業額'], '-o',label='平日營業額') #給予線標籤
plt.plot(data['時間'], data[' 週末營業額'], '-o', label='週末營業額') #給予線標籤
plt.xticks(fontsize=15,rotation=90)
plt.grid(True) # grid 開啟
plt.xlabel('時間（0-24點）',fontsize=15)
plt.ylabel('營業額',fontsize=15)
plt.title('營業額的視覺化',fontsize=30)
plt.legend(bbox_to_anchor=(1.03, 0.8), loc=2) #開啟圖例
plt.show()

