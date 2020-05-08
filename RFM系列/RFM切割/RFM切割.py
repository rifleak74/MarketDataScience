#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:32:20 2020

@author: ivan
"""
import pandas as pd
import datetime
import numpy as np

orders = pd.read_csv('orders.csv')
#空值該列全部刪除
orders.dropna(inplace = True)


##### 算出每個客戶的購買清單 #####
# pivot_table：計算每個人在banana、water與milk的消費數量
orders['values'] = 1
purchase_list = orders.pivot_table(index=['clientId','gender','orderdate'], #分類條件
                          columns='product', # 目的欄位
                          aggfunc=sum, # 計算方式，max, min, mean, sum, len
                          values='values' #根據欄位
                          ).fillna(0).reset_index()

##### 最近一次消費計算 #####
# 設定今天的日期為最近一位顧客購買的日期，從那天來看過往的銷售狀況
theToday = datetime.datetime.strptime(orders['orderdate'].max(), "%Y-%m-%d")
# 將購買清單資料中'orderdate'的欄位，全部轉換成datetime格式
purchase_list['orderdate'] = pd.to_datetime(purchase_list['orderdate'])
# 計算消費者至今再次購買與上次購買產品的時間差'
purchase_list['recency'] =( theToday - purchase_list['orderdate'] ).astype(str)
# 將'recency'欄位中的days去除
purchase_list['recency'] = purchase_list['recency'].str.replace('days.*', #想取代的東西
                                                                  '', #取代成的東西
                                                                  regex = True)
# 將'recency'欄位全部轉換成int
purchase_list['recency'] = purchase_list['recency'].astype(int)


##### 計算購買間隔 #####
purchase_list['interval'] = purchase_list.groupby("clientId", #分類條件
                                  as_index = True # 分類條件是否要取代Index
                                  )['orderdate'].diff()
purchase_list.dropna(inplace = True)#刪除第一次來本店的資料
purchase_list['interval'] = purchase_list['interval'].astype(str) # 將時間資料轉成字串
purchase_list['interval'] = purchase_list['interval'].str.replace('days.*', '').astype(int) #將欄位中的days去除


purchase_list['interval'].describe()
purchase_list['interval'].quantile([0.25, 0.5, 0.75])
purchase_list['interval'].quantile([0.16, 0.32, 0.5, 0.66, 0.82])
