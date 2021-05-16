# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:44:21 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第七章 Jieba切詞工具
TF-IDF關鍵字分析
"""
import jieba.analyse

text = '''
行銷的市場
越來越競爭
Python成了每個人必要的武器
雖然說程式的市場也是很競爭
而且程式學起來很痛苦
不要怕跟我走
我們一起走向新零售吧！'''

#--- 關鍵詞提取
keywords1=jieba.analyse.extract_tags(text)
print("/ ".join(keywords1))

# top 3 關鍵字
keywords_top=jieba.analyse.extract_tags(text, # 字詞
                                        topK=3, # 前幾名
                                        withWeight=True) # 是否要計算分數