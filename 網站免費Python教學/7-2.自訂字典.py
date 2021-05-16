# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:43:27 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第七章 Jieba切詞工具
自訂字典
"""
import jieba

#--- 切詞的弊端
# 簡體對照繁體會有一些問題
text = '''
行銷的市場
越來競爭
Python成了每個人必要的武器
我們一起走向新零售吧！'''
words = jieba.cut(text)
print("/ ".join(words))


#--- 使用繁體字典
jieba.set_dictionary('dict.txt.big')

# 再次重新切割
words = jieba.cut(text)
print("/ ".join(words))