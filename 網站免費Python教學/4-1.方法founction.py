# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 11:45:45 2021

@author: Ivan
內容來自：行銷搬進大程式
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第四章Python模組與套件概念
方法founction
"""

# 問題：用程式實現機率「c的X取Y」
# 10!/(10-2)! * 2!
#----- 土法煉鋼寫法 -----
x = 10
y = 2
# 計算10!
count1 = 1
for i in range(1, x+1):
    count1 = count1 * i
# 計算(10-2)!
count2 = 1
for i in range(1, x-y+1):
    count2 = count2 * i
# 計算2!
count3 = 1
for i in range(1, y+1):
    count3 = count3 * i
c = count1 / (count2 * count3)


#----- def方法寫法 -----
x = 10
y = 2
# 階層計算機
def factorial(n):
    """
    參數n：欲計算階層的尾數
    範例：計算10!，n輸入10
    """
    count = 1
    for i in range(1, n+1):
        count = count * i
    return count
c = factorial(x) / (factorial(x-y) * factorial(y))