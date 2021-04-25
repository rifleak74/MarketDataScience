# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 17:31:19 2021

@author: Ivan
內容來自：行銷搬進大程式
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第四章Python模組與套件概念
匯入import
"""
# 匯入套件，也就是整個檔案程式碼
import mymath
x = 10
y = 2
c = mymath.factorial(x) / ( mymath.factorial(x-y) *  mymath.factorial(y))

# as：取小名，不想打太長的套件名稱所使用
import mymath as mm
x = 10
y = 2
c = mm.factorial(x) / ( mm.factorial(x-y) *  mm.factorial(y))

# 從套件中獲取「特定」方法
from mymath import factorial
x = 10
y = 2
c = factorial(x) / (factorial(x-y) * factorial(y))

# 從套件中獲取「多個」方法
from mymath import factorial, accumulate
x = 10
y = 2
c = factorial(x) / (factorial(x-y) * factorial(y))