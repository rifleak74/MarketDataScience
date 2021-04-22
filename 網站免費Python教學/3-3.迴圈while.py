# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 11:28:32 2021

@author: Ivan
內容來自：行銷搬進大程式
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第三章Python流程控制教學
迴圈while
"""
# while設計方式
i = 0 # 需要有一個容器
while i < 10 : # 判斷式
    print(i)
    i = i + 1 # 容器需要變化

# 無窮迴圈
i = 0
while i < 10 :
    print(i)

# 無窮迴圈2
while True :
    print('這是無窮迴圈～～～')
    
# while迴圈與if判斷式的結合
i = 0
while i < 10 :
    if i % 2 == 0:
        print(i)
    i = i + 1 # 容器需要變化

# 製作斷點
i = 0
while i < 10 :
    if i % 2 == 0:
        if i == 4:
            break; # 斷點
        print(i)
    i = i + 1 # 容器需要變化