# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:51:34 2021

@author: Ivan
內容來自：行銷搬進大程式
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第四章Python模組與套件概念
匯入import
"""

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

# 累加計算機
def accumulate(n):
    """
    參數n：欲計算累加的尾數
    範例：計算1+2+3...+10，n輸入10
    """
    return (1+n)*n/2