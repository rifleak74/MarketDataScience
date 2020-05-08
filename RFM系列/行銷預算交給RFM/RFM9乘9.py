# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 20:06:33 2019

@author: Ivan
"""

import pandas as pd

# 必須先設定中文文字檔，請參考https://bit.ly/2Y1cZIQ
import matplotlib.pyplot as plt
import seaborn as sns 
#設定圖片為中文
sns.set(font='sans-serif')
sns.set_style("whitegrid",{"font.sans-serif":['Microsoft JhengHei']})

#此檔案請下在另外附檔
purchase_list= pd.read_csv('purchase_list.csv', encoding='utf-8')




##### 切割 recency、frequency #####
# 切割 recency
cut = 9 #切割條件
recency_label = []
recency_tolerance = int(purchase_list['recency'].max()/cut)

for i in range( cut-1):
    recency_label.append(str(i*recency_tolerance) + '-' + str(i *recency_tolerance+recency_tolerance-1) + ' day')

# 加上最後一位
recency_label.append(str((i+1)*recency_tolerance) + '-' + str(purchase_list['recency'].max()) + ' day')

purchase_list['recency_cate'] = pd.cut( 
        purchase_list['recency'] , #目標欄位
        cut, #切割條件
        labels =recency_label) #切割後的分類內容

# 切割 frequency
frequency_label = []
frequency_tolerance = int(purchase_list['frequency'].max()/cut)


for j in range( cut-1):
    frequency_label.append(str(j*frequency_tolerance+1) + ' freq')

    
# 加上最後一位
frequency_label.append('>' + str(j*frequency_tolerance+1) + ' freq')

purchase_list['frequency_cate'] = pd.cut( 
        purchase_list['frequency'] , #目標欄位
        cut,  #切割條件
        labels =frequency_label) #切割後的分類內容

##### 繪圖部分 #####
df3 = pd.melt(purchase_list.drop(columns = ['orderdate','recency','frequency']), id_vars=['clientId','recency_cate','frequency_cate','gender'], var_name='types', value_name='values') 
df3['values'] = pd.to_numeric(df3['values'],errors='coerce')
df3 = df3.dropna()


#先設定畫布大小
fig, axes = plt.subplots(cut, cut,figsize=(25,15))
countX = 0 # 畫布X軸座標
for i in frequency_label[::-1]: # 由於axes畫布排列的關係，頻率必須要反著放
    countY = 0 # 畫布Y軸座標
    for j in recency_label: # 近因
        if df3[(df3['recency_cate']==j) & (df3['frequency_cate']==i)].shape[0] != 0: # 檢查這個方格有沒有數據
            
            # 處理堆疊數據，將該小區塊的購買量，換算成百分比
            df4 = df3[(df3['recency_cate']==j) & (df3['frequency_cate']==i)] #先找出所有符合該小區域的資料
            df4 = df4.groupby(['types', 'gender'])['values'].sum() # 依照不同的性別，做商品購買量的加總
            df4 =df4.groupby(level=1).apply(lambda x:100 * x / float(x.sum())) # 將其數量換成百分比
            df4 = df4.add_suffix('').reset_index() #將三圍度改為二圍度
            df4=df4.pivot('gender', 'types', 'values') # XY軸交換表示
            # 以下為單一小圖表的設定
            sns.barplot(x="types", # 小圖表X資料來源欄位
                        y="values", # 小圖表Y資料來源欄位
                        data=df3[(df3['recency_cate']==j) & (df3['frequency_cate']==i)], #來源資料表
                        capsize=.2, # 最高點最低點的大小
                        ax=axes[countX, countY]) # 小圖表座標
            
            #將水、牛奶、香蕉的字變大
            axes[countX][countY].tick_params(labelsize=7)
            #使所有數據的尺碼相同
            axes[countX][countY].set_yticks(range(int(df3['values'].max())))
            
            # 畫X標籤
            if i == frequency_label[0]:
                axes[countX][countY].set_xlabel(j, fontsize=17)
                
            # 畫Y標籤
            if j == recency_label[0]:
                axes[countX][countY].set_ylabel( frequency_label[::-1][countX], fontsize=17)
            else:
                axes[countX][countY].set_ylabel('')


        countY +=1
    countX += 1 
fig.suptitle('RFM-商品分類圖', position=(.5,1), fontsize=35) # 設定標題
fig.text(0.5, 0.01, '光顧天數', ha='center', va='center', fontsize=20) # 設定X軸標題
fig.text(0.01, 0.5, '購買頻率', ha='center', va='center', rotation='vertical', fontsize=20) # 設定Y軸標題
fig.show()


#產出常貴客名單
df5 = purchase_list[purchase_list['recency']<9]  
df6 = df5[df5['frequency']>8]
df6.to_csv("常貴客名單.csv",encoding='utf-8')