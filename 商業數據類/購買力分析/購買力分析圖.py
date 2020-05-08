# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 15:55:51 2020

@author: Ivan
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
colrogroup = ['#427f8f','#4a8fa1','#559db0','#66a7b8','#77b1c0','#89bbc8','#9ac5d0','#bdd9e0','#cee3e8','#e0edf0']

#讀取檔案
order = pd.read_csv('orders.csv')

#查看甚麼產品的銷量最好
order['product'].value_counts()

#查看哪位顧客在我公司花最多錢
thesum = order.groupby("clientId", #分類條件
                        as_index = False # 分類條件是否要取代Index
                        )['grossmarg'].sum() # 目的欄位 & 計算方式，max, min, mean, sum
thesum.columns = ['顧客ID','總消費金額']
#查看顧客平均花多少錢在公司
themean = order.groupby("clientId", #分類條件
                        as_index = False # 分類條件是否要取代Index
                        )['grossmarg'].mean() # 目的欄位 & 計算方式，max, min, mean, sum
themean.columns = ['顧客ID','平均消費金額']

enddata = pd.concat([thesum, themean['平均消費金額']],axis=1)

#--- 繪製購買力分析圖
plt.scatter(enddata['平均消費金額'],enddata['總消費金額'], 
            color='#427f8f',
            alpha=0.5)
plt.plot(np.arange(0, 50, 0.5), color='#c888bb', linestyle='dashed', linewidth=2) # 繪製線
plt.plot(np.arange(0, 50, 1), color='#88c895', linestyle='dashed', linewidth=2) # 繪製線
plt.plot(np.arange(0, 50, 2), color='#c89588', linestyle='dashed', linewidth=2) # 繪製線

plt.title("購買力分析圖",fontsize=30)#標題
plt.ylabel("總消費金額",fontsize=20)#y的標題
plt.xlabel("平均消費金額",fontsize=20) #x的標題
plt.grid(True) # grid 開啟
plt.tight_layout()
