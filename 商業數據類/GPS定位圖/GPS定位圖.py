import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'sans-serif' 
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 

# 設定顏色
colorcompetitor = ['#d9f776','#76f794','#9476f7','#f776d9','#e70e4b','#76d9f7','#f79476','#fbccbe']
 

searchbrand=['N','S','A','U2','M','T','D','U']
a=          [0.16,0.13,0.34,0.29,0.4,0.26,0.21,0.13]
b=          [0.14,0.18,0.16,0.15,0.28,0.14,0.26,0.04]
area =      [1225,1600,400,400,324,400,400,25]
sh=plt.scatter(a,b,s=area,c=colorcompetitor,alpha=0.5)
ax = plt.gca()
plt.axvline(np.mean(a), color='c', linestyle='dashed', linewidth=1) # 繪製平均線
plt.axhline(np.mean(b), color='c', linestyle='dashed', linewidth=1) # 繪製平均線
plt.title("品牌定位圖_舒適&時尚",fontsize=30)
plt.ylabel('舒適',fontsize=15)
plt.xlabel('時尚',fontsize=15)
for j in range(len(searchbrand)):
    plt.text(a[j], b[j], '%s' % searchbrand[j], fontsize=10 )
plt.show()
