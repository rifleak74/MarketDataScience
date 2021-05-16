# -*- coding: utf-8 -*-
"""
Created on Sun May 16 11:40:16 2021

@author: Ivan
https://marketingliveincode.com/
版權屬於「行銷搬進大程式」所有，若有疑問，可聯絡ivanyang0606@gmail.com

Python免費基礎教學課程
第七章 Jieba切詞工具
Jieba切詞基本概念
"""
import jieba

#--- 結巴切詞工具
cut_list = jieba.cut("小明硕士毕业于中国科学院计算所，后在日本京都大学深造") 
print("/ ".join(cut_list)) # 當陣列顯示出來
