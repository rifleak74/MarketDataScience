#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:59:05 2020

@author: ivan
"""
import pandas as pd
from apyori import apriori
from tqdm import tqdm

order_products = pd.read_csv('order.csv', encoding='utf-8')

record=[]
for i in tqdm(order_products['order_id'].value_counts().index):
    member = order_products[order_products['order_id']==i]
    record.append(member['product_name'].values.tolist())   
association_rules = apriori(record, min_support=0.01, min_lift=1.0000001)
association_results = list(association_rules)

#挑出第一筆資料
list1 = association_results[0]

print('商品組合： ')
print(list1[0])

print('這個組合的支持度： ')
print(list1[1])

print('以Bag of Organic Bananas產品為出發點的信賴度： ')
print(list1[2][0][2])

print('以Bag of Organic Bananas產品為出發點的提昇度： ')
print(list1[2][0][3])

print('以Large Lemon產品為出發點的信賴度： ')
print(list1[2][1][2])

print('以Large Lemon產品為出發點的提昇度： ')
print(list1[2][1][3])

#將結果轉成Dataframe格式
association_DF = pd.DataFrame(association_results)

association_DF['ordered_statistics']
association_DF = association_DF.explode('ordered_statistics')
association_DF['A產品'] = association_DF['ordered_statistics'].str[0]
association_DF['B產品'] = association_DF['ordered_statistics'].str[1]
association_DF['信賴度'] = association_DF['ordered_statistics'].str[2]
association_DF['提昇度'] = association_DF['ordered_statistics'].str[3]
