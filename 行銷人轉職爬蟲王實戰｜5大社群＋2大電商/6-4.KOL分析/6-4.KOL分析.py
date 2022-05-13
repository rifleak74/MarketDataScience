# -*- coding: utf-8 -*-
"""
Created on Sun May 23 12:51:24 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第六章 Youtube中尋找KOL夥伴
KOL分析
"""
import datetime
import matplotlib.pyplot as plt
import pandas as pd
#設定時間
today = datetime.datetime.today()

# 取得資料
getdata = pd.read_csv('Youtuber_頻道資料.csv', encoding = 'utf-8-sig')
getdata.columns

# 處理經營時間欄位
getdata['開始經營時間'] = pd.to_datetime(getdata['開始經營時間'])
getdata['經營天數'] = (today - getdata['開始經營時間']).astype(str)
getdata['經營天數'] = getdata['經營天數'].str.replace('days.*', #想取代的東西
                                                    '', #取代成的東西
                                                    regex = True)
getdata['經營天數'] = getdata['經營天數'].astype(int)

# 處理總觀看數欄位
getdata['總觀看數'] = getdata['總觀看數']/10000

# 處理總訂閱數欄位
getdata['總訂閱數'] = getdata['總訂閱數'].str.replace('萬', #想取代的東西
                                                    '', #取代成的東西
                                                    )
getdata['總訂閱數'] = getdata['總訂閱數'].astype(float)

#進行資料分析－四象限分析
plt.figure(figsize=(20,10))
colorlist = []
for tx,ty,ab in zip(getdata['總訂閱數'],getdata['總觀看數'], getdata['Youtuber頻道名稱']):
    Aavg = getdata['總訂閱數'].mean()
    Bavg = getdata['總觀看數'].mean()
    
    if (tx < Aavg) & (ty < Bavg):#第三象限
        colorlist.append('#abc4d8')
    elif (tx > Aavg) & (ty < Bavg):
        colorlist.append('#abd8bf')
    elif (tx < Aavg) & (ty > Bavg):
        colorlist.append('#d8bfab')
    else:
        colorlist.append('#d8abc4')
    plt.text(tx,ty,ab, fontsize=15)# 加上文字註解
# 繪製圓點
plt.scatter(getdata['總訂閱數'],getdata['總觀看數'],
            color= colorlist,
            s=getdata['經營天數'],
            alpha=0.5)

plt.axvline(getdata['總訂閱數'].mean(), color='c', linestyle='dashed', linewidth=1) # 繪製平均線    
plt.axhline(getdata['總觀看數'].mean(), color='c', linestyle='dashed', linewidth=1) # 繪製平均線 


plt.title("KOL分析",fontsize=30)#標題
plt.ylabel('總觀看數',fontsize=20)#y的標題
plt.xlabel('總訂閱數',fontsize=20) #x的標題
plt.tight_layout()

#進行資料分析－正比分析
plt.figure(figsize=(20,10))
colorlist = []
for tx,ty,ab in zip(getdata['總訂閱數'],getdata['總觀看數'], getdata['Youtuber頻道名稱']):
    Aavg = getdata['總訂閱數'].mean()
    Bavg = getdata['總觀看數'].mean()
    
    if (tx < Aavg) & (ty < Bavg):#第三象限
        colorlist.append('#abc4d8')
    elif (tx > Aavg) & (ty < Bavg):
        colorlist.append('#abd8bf')
    elif (tx < Aavg) & (ty > Bavg):
        colorlist.append('#d8bfab')
    else:
        colorlist.append('#d8abc4')
    plt.text(tx,ty,ab, fontsize=15)# 加上文字註解
# 繪製圓點
plt.scatter(getdata['總訂閱數'],getdata['總觀看數'],
            color= colorlist,
            s=getdata['經營天數'],
            alpha=0.5)
plt.plot([0, 400], [0, 80000] ,
         color='c', 
         linestyle='dashed', 
         linewidth=1
    )

plt.title("KOL分析",fontsize=30)#標題
plt.ylabel('總觀看數',fontsize=20)#y的標題
plt.xlabel('總訂閱數',fontsize=20) #x的標題
plt.tight_layout()