import pandas as pd
import datetime
import numpy as np

# 必須先設定中文文字檔，請參考https://bit.ly/2Y1cZIQ
import matplotlib.pyplot as plt
import seaborn as sns 
#設定圖片為中文
sns.set(font='sans-serif')
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})

#此檔案請下在另外附檔
purchase_list= pd.read_csv('purchase_list.csv', encoding='utf-8')

recency_label =  ['0-7 day', '8-15 day', '16-22 day', '23-30 day', '31-55 day', '>55 day']
frequency_label =  ['1 freq', '2 freq', '3 freq', '4 freq', '5 freq', '>5 freq']
g = sns.FacetGrid(purchase_list, # 來源資料表
                  col="recency_cate", # X資料來源欄位
                  row="frequency_cate" ,  # Y資料來源欄位
                  col_order= recency_label,  # X資料順序
                  row_order= frequency_label[::-1], # Y資料順序
                  margin_titles=True)
#小圖表部分
g = g.map_dataframe(sns.barplot, # 資料顯示的模式
                    x= 'gender', # 小圖表X資料來源
                    y ='購買量', # 小圖表Y資料來源
                    palette = sns.color_palette("muted")) #畫布色調

g = g.set_axis_labels('光顧天數','購買頻率').add_legend()