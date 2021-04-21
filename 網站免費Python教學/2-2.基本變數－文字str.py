# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:02:33 2021

@author: Ivan
內容來自：行銷搬進大程式
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第二章Python基本變數教學
基本變數－文字str
"""

# 單引號「'」或雙引號「"」包覆起來成為文字str
boxname1 = '這是一串文字'
boxname2 = "這也是是一串文字"

# 字串相加
boxname3 = boxname1 + boxname2

# 不同型態相加
boxname1 + 1
boxname1 + str(1)

# 取出字串
takestr = '我要嘗試看看自己取字串'
takestr[2:5] #取中間
takestr[2:] # 從第2取到底
takestr[:5] # 從開頭取到第5
takestr[:-2] # 從開頭取到倒數第2
