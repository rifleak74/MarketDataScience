# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 09:35:15 2021

@author: Ivan
內容來自：行銷搬進大程式
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第三章Python流程控制教學
判斷式If
"""

# 布林
a = 10
b = 3

a > b # 大於
a < b # 小於
a == b # 等於
a != b # 不等於

# 邏輯運算
not(a > b)
a > b or a < b
a > b and a < b

# if判斷式
if a > b:
    print('a是有大於B的')
else:
    print('a小於b')
    
# 多層if判斷
if b == 10:
    print('b的內容是10')
elif b > 10:
    print('b比10還大')
else:
    print('b小於10吧！')
    
# if應用在字串比較
thestr = '我們來練習字串比較'
if '字串' in thestr:
    print('有在裡面喔！')
    
# if應用在陣列
thelist = ['我','們','來練習','字串比較']
if '字串' in thelist:
    print('有在裡面喔！')
    
# if加上邏輯運算
if ('字串' in thestr) and ('字串' in thelist):
    print('兩者裡面都有字串這個字')