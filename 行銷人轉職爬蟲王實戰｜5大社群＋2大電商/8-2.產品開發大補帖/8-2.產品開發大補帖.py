# -*- coding: utf-8 -*-
"""
Created on Thu May 20 10:14:30 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第八章 shapee市場預估－這個市場有多大？
產品開發大補帖
"""
import pandas as pd

#--- 匯入資料
comment_data = pd.read_csv('花襯衫_留言資料.csv')
# 查看資料欄位
comment_data.columns

#先取代同意詞語
#先取代全形字母
comment_data['商品規格'] = comment_data['商品規格'].str.replace('Ｓ','S')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('Ｍ','M')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('Ｌ','L')

#從最大的開始取代（大尺碼）
comment_data['商品規格'] = comment_data['商品規格'].str.replace('XXXXXXXXL','8@')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('8XL','8@')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('XXXXXXXL','7@')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('7XL','7@')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('XXXXXXL','6@')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('6XL','6@')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('XXXXXL','5@')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('5XL','5@')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('XXXXL','4@')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('4XL','4@')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('XXXL','3@')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('3XL','3@')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('XXL','2@')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('2XL','2@')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('XL','1@')

#從最小的開始取代（小尺碼）
comment_data['商品規格'] = comment_data['商品規格'].str.replace('XXS','3~')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('3XS','3~')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('XS','2~')

#取代特殊顏色
comment_data['商品規格'] = comment_data['商品規格'].str.replace('深灰','1#')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('熒光綠','2#')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('軍綠色','3#')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('酒紅','4#')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('深藍','5#')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('墨綠','6#')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('粉橘','7#')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('紫粉','8#')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('棗紅','9#')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('寶藍','10#')
comment_data['商品規格'] = comment_data['商品規格'].str.replace('卡其','11#')

comment_data['商品規格'] = comment_data['商品規格'].str.replace('桃紅','桃')

color = ['黑','白','灰','綠','粉色','膚','橘','藍','紫色','咖啡色','焦糖','桃','紅'
         ,'黃','藏青','杏','1#','2#','3#','4#','5#','6#','7#','8#','9#','10#','11#']
size = ['8@','7@','6@','5@','4@','3@','2@','1@','L','M','S','2~','3~']

#--- 範例：如何決定口罩產品線開發SUK
def evaluation(thestr):
    return eval(thestr) # 轉換str中的內容真正型態

comment_data['商品規格'] = comment_data['商品規格'].apply(evaluation) # 將dataframe的資料內容套入方法
allpro = comment_data['商品規格'].sum() # 將所有消費者購買過的商品合併在一個list
allpro = pd.DataFrame(allpro) # 轉成dataframe格式
allpro.dropna(inplace=True) # 移除空值

#--- 創造市場SKU統計表
counter=[]
for c in color:
    container=[]
    for s in size:
        container.append(
            len(allpro[ allpro[0].str.contains(c) &
                        allpro[0].str.contains(s)
                       ])
            )
    counter.append(container)
    
# 產品開發大補帖完成
buyer = pd.DataFrame(counter)
buyer.columns = ['8XL','7XL','6XL','5XL','4XL','3XL','2XL','1XL','L','M','S','2XS','3XS']
buyer.index = ['黑','白','灰','綠','粉色','膚','橘','藍','紫色','咖啡色',
               '焦糖','桃','紅' ,'黃','藏青','杏','深灰','熒光綠','軍綠色',
               '酒紅', '深藍','墨綠','粉橘','紫粉','棗紅','寶藍', '卡其']
