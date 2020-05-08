# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 16:20:06 2020

@author: Ivan
"""

from google.cloud import language
from google.cloud.language import enums
import os

text= '想與姊妹掏來個下午茶談天時光，應該不少人都會想到咖啡廳聚集地 - 捷運中山站，除了幾間著名大家耳熟能詳的咖啡'
# （因為過多，詳情請看github程式碼，以下省略...）
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '你的憑證檔案名稱.json'
# 實例化一個客戶端
client = language.LanguageServiceClient()
type_ = enums.Document.Type.PLAIN_TEXT

language = "zh-Hant"
document = {
    "content": text,
    "type": type_,
    "language": language}

# 設定編碼
encoding_type = enums.EncodingType.UTF8
response = client.analyze_entities(document, encoding_type=encoding_type) #進行計算

for entity in response.entities:
    print("詞: " + entity.name)
    print("詞語型態: " + enums.Entity.Type(entity.type).name)
    print("重要性: " + str(entity.salience))
