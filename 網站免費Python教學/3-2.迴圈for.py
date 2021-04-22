# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 09:59:06 2021

@author: Ivan
內容來自：行銷搬進大程式
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第三章Python流程控制教學
迴圈for
"""
# for迴圈的輸出邏輯
for i in [0,1,2,3,4,5,6,7]:
    print(i)

# 與前者相同
thelist = [0,1,2,3,4,5,6,7]
for i in thelist:
    print(i)
    
# 與前者相同
for i in range(8): # range(開始, 結束, 公差)
    print(i)

# 與前者相同
thelist = [0,1,2,3,4,5,6,7]
for i in range(len(thelist)):
    print(thelist[i])

# 應用：創造壘加
container = 0
for i in range(8):
    container = container + i
    
# for 與 if 做結合
thelist = [0,1,2,3,4,5,6,7]
for i in range(len(thelist)):
    if thelist[i] % 2 == 0:
        print(thelist[i])
        
# 製作斷點
thelist = [0,1,2,3,4,5,6,7]
for i in range(len(thelist)):
    if thelist[i] % 2 == 0:
        if thelist[i] == 4:
            break; # 斷點
        else:
            print(thelist[i])

# 製作跳過
thelist = [0,1,2,3,4,5,6,7]
for i in range(len(thelist)):
    if thelist[i] % 2 == 0:
        if thelist[i] == 4:
            continue; # 跳過
        else:
            print(thelist[i])

# 雙重迴圈
for i in range(5):
    for j in range(5):
        print('I：' + str(i) + ' J：' + str(j))
        
# 應用：99乘法表
for i in range(9):
    for j in range(9):
        print(str(i) + ' x ' + str(j) + ' = ' + str(i*j))