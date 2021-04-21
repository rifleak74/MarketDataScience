# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:13:08 2021

@author: Ivan
內容來自：行銷搬進大程式
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第二章Python基本變數教學
基本變數－陣列List
"""

# 陣列中的型態不限制
boxname1 = [1,2,3,4,5]
boxname2 = ['你','好','我','是','陣列']
boxname3 = [[1,2,3],4,5]
boxname4 = [1,
            '都可以放',
              [
                ['A','B'],
                [2,3]
              ]
            ]

#取出陣列內資料
boxname1[3]
boxname2[0]
boxname3[0][2]
boxname3[-1] # 從後面取

# 陣列中新增資料
boxname1.append(3)
boxname1.append(8)
boxname1.append(4)
boxname2.extend(boxname3) # 將另一個陣列插在最後面

# 陣列內容排序
boxname1.sort()

# 刪除陣列內容
del boxname1[0]
boxname1[0] # 資料順延
boxname1.remove(4) # 指定刪除
boxname1.pop() # 只刪除最後一個
