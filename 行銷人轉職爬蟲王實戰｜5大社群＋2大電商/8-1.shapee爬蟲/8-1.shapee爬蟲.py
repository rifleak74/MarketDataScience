# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:02:59 2021
@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com
第八章 shapee市場預估－這個市場有多大？
shapee爬蟲
"""
import requests
import json
import pandas as pd
import time
# selenium，2022/9/17 將套件更新到4.4.3版本，因此寫法全部都更新過
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import re
import random

keyword = '花襯衫'
page = 10
ecode = 'utf-8-sig'

# 2022/11/21 由於蝦皮API更新，加上了不少認證機制，因此在爬蟲之前，請先將header換成自己的
my_headers = {
    'accept': 'application/json',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'af-ac-enc-dat': 'AAcyLjQuMS0zAAABhKHhedEAAAtaAk4AAAAAAAAAAAvjwIqTsIlqbAt1di/KUNkkDfbrGH0dFr4BNqSRFEryKlpQoLPyGTqmXqL5F/8SvcTp8K6TCnpSZk1H9ceC295JHXrjVKy54uYqF/6KFSsRJsilt8Bl4VIIFFyt8ulG8UJIxlZGjuvBxpCGq/7Ekqct2WHRhYqwgcI+TgqizPqXvcUXZVbatanxNH0gKodDr23p0E7FOEJgWHqhRCLDJkB0UgDz+xhpe28iS3zrEtxrnqOCipnpmbrVxCJ6Cg53vZNG5GgQ+HsLteH6eVU3KBRO6TUWVKy54uYqF/6KFSsRJsilt/DWXQ/ZsonAkSLw3BL0KigMODMAZRB5xF24FfGUuTRRL5hL53sDq8dM1mFhQyMOoC2I+h6ztg/SjtkCe2K567gSHQ7iuYowyMydx8exDaeCF+8hpeeDkMDl0WXkPHJxWR0ankyqY5ve5FWxWem2DQKRY7OMsPKRljZ2EI7Zp6aWkWOzjLDykZY2dhCO2aemlu6SQ5byQJi4sOtAYkOvWutmD1Ju5IMO/YH/7c70+qrpF+8hpeeDkMDl0WXkPHJxWRhIsbkcqJR6nS23b0O/1wgobW0+BI9V4CXqmdYH0r6N+5mfYG1KcJ74vyUyUxtl8HThxt8jVqlA/krRnxthvDZfXPbPIRpzxH49wF3Wr3bHWXmYr7/dXjod4whdsMTLghsXMtlet6Ih+KndfWkuB2iRY7OMsPKRljZ2EI7Zp6aWaqqMl5VUdXB6xw5O5xrlspKvcaK/fDy4KzZ4lWl+sI9QJ2vX7vXsIPRiLtp+87ve',
'content-type': 'application/json',
'cookie': '__LOCALE__null=TW; SPC_R_T_ID=+7UdyVmMrkVRqO7k8i2prG6AwhuJu337u9VLj5unTJDGtau+tTU8DOxnSHKT/ZvKqOgaeeyml/Cc3QuH+Gu6cdAerdRA5WBoPP2QBYPFd+KsG8NRQnD7utW1GGa6km/uodyV7uIXOXZSnsnnlRyVoEKzESkih0/0kv6frm+0PZ4=; SPC_R_T_IV=RWRHQ3dFaUpZZ3VLT2VBYg==; SPC_T_ID=+7UdyVmMrkVRqO7k8i2prG6AwhuJu337u9VLj5unTJDGtau+tTU8DOxnSHKT/ZvKqOgaeeyml/Cc3QuH+Gu6cdAerdRA5WBoPP2QBYPFd+KsG8NRQnD7utW1GGa6km/uodyV7uIXOXZSnsnnlRyVoEKzESkih0/0kv6frm+0PZ4=; SPC_T_IV=RWRHQ3dFaUpZZ3VLT2VBYg==; SPC_SI=MLh0YwAAAABLYkUzV1o2MBrxjAAAAAAAYzB5Vnh1MkI=; SPC_F=dwcS7qZ6lde6REiKJH1yl8F4Wj71GWH5; REC_T_ID=6a52d349-6ac5-11ed-b583-b47af14a882c; csrftoken=3xxjtUDsRP2gv98Z62R3uQiT8XOm3E0p; _QPWSDCXHZQA=76295ff1-5367-4f7d-acf7-ffd877388871; _gcl_au=1.1.1924617676.1669163167; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.1680480979.1669163170; _fbp=fb.1.1669163170334.247136174; _ga=GA1.1.870225610.1669163168; shopee_webUnique_ccd=XIrBEty%2BNaCWfXlB5ZleKA%3D%3D%7CGEp2Na4rC%2B%2BCny4XlOrUt7maIwDZ8cwSzouWrz1as7qJmVKLUrDvQGcDPQKmHqjAUGFgE2rBpgMZz76iOvwyCNXGJK%2FWeZXuhrxr%7C2Rfhhu0BdUx6OmV0%7C06%7C3; ds=f61296f150d94957950d4280b76174e8; _ga_RPSBE3TQZZ=GS1.1.1669163167.1.1.1669163242.60.0.0; cto_bundle=1riUq19pTjNPTjZxZmlyckMwTkNWODByTWRhU3R5U0xNdXh5SmdKUUdJTUtoOGhaUVJEOVZQMktqWmhkQkJNQlZHdW92a3VHNU9WM1JSOUZhSFV6WjBsbEVKREZJQ0VPSmYlMkZyV0dYbG1PODFMb0VwOUtJZ3ZHaXZsQnNvQWJRa240MFZ2dlo1Y0FNVlR3WE84cDdHYXElMkZZZyUyRlElM0QlM0Q',
'referer': 'https://shopee.tw/50%E6%AC%BE%E5%8F%AF%E9%81%B8-%E7%94%B7%E7%94%9F%E5%A4%8F%E5%AD%A3%E4%BC%91%E9%96%92-%E5%A4%8F%E5%A4%A9%E8%A1%A3%E6%9C%8D-%E8%A5%AF%E8%A1%A3-%E5%A4%8F%E5%A8%81%E5%A4%B7%E7%9F%AD%E8%A2%96%E8%A5%AF%E8%A1%AB-%E5%BA%A6%E5%81%87%E9%A2%A8%E8%A5%AF%E8%A1%AB-%E7%9F%AD%E8%A2%96%E8%A5%AF%E8%A1%AB-M-3XL-%E8%8A%B1%E8%A5%AF%E8%A1%AB-%E6%83%85%E4%BE%B6%E8%A5%AF%E8%A1%AB-%E4%BA%94%E5%88%86%E8%A2%96%E8%A5%AF%E8%A1%AB-i.718087400.18213582177?sp_atk=fb7fa29a-4f26-4817-8a18-a49769075a55&xptdk=fb7fa29a-4f26-4817-8a18-a49769075a55',
'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'sz-token': 'XIrBEty+NaCWfXlB5ZleKA==|GEp2Na4rC++Cny4XlOrUt7maIwDZ8cwSzouWrz1as7qJmVKLUrDvQGcDPQKmHqjAUGFgE2rBpgMZz76iOvwyCNXGJK/WeZXuhrxr|2Rfhhu0BdUx6OmV0|06|3',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
'x-api-source': 'pc',
'x-csrftoken': '3xxjtUDsRP2gv98Z62R3uQiT8XOm3E0p',
'x-requested-with': 'XMLHttpRequest',
'x-shopee-language': 'zh-Hant'
      }     

# 進入每個商品，抓取買家留言
def goods_comments(item_id, shop_id):
    # url = 'https://shopee.tw/api/v2/item/get_ratings?itemid='+ str(item_id) + '&shop_id=' + str(shop_id) + '&offset=0&limit=200&flag=1&filter=0'
    url = 'https://shopee.tw/api/v2/item/get_ratings?filter=0&flag=1&itemid='+ str(item_id) + '&limit=50&offset=0&shopid=' + str(shop_id) + '&type=0'
    r = requests.get(url,headers = my_headers)
    st= r.text.replace("\\n","^n")
    st=st.replace("\\t","^t")
    st=st.replace("\\r","^r")
    
    gj=json.loads(st)
    return gj['data']['ratings']
    

# 進入每個商品，抓取賣家更細節的資料（商品文案、SKU）
def goods_detail(item_id, shop_id):
    url = 'https://shopee.tw/api/v4/item/get?itemid=' + str(item_id) + '&shopid=' + str(shop_id)
    r = requests.get(url,headers = my_headers)
    st= r.text.replace("\\n","^n")
    st=st.replace("\\t","^t")
    st=st.replace("\\r","^r")
    
    gj=json.loads(st)
    return gj


# 自動下載ChromeDriver
service = ChromeService(executable_path=ChromeDriverManager().install())

# 關閉通知提醒
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

# 開啟瀏覽器
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
time.sleep(5)

# 開啟網頁
driver.get('https://shopee.tw/search?keyword=' + keyword )
time.sleep(10)


print('---------- 開始進行爬蟲 ----------')
tStart = time.time()#計時開始

container_product = pd.DataFrame()
container_comment = pd.DataFrame()
for i in range(int(page)):

    # 準備用來存放資料的陣列
    itemid = []
    shopid =[]
    name = []
    brand = []
    stock = []
    price = []
    ctime = []
    description = []
    discount = []
    can_use_bundle_deal = []
    can_use_wholesale = []
    tier_variations = []
    historical_sold = []
    is_cc_installment_payment_eligible = []
    is_official_shop = []
    is_pre_order = []
    liked_count = []
    shop_location = []
    SKU = []
    cmt_count = []
    five_star = []
    four_star = []
    three_star = []
    two_star = []
    one_star = []
    rating_star = []
    
    driver.get('https://shopee.tw/search?keyword=' + keyword + '&page=' + str(i))

    # 滾動頁面
    for scroll in range(6):
        driver.execute_script('window.scrollBy(0,1000)')
        time.sleep(2)
    
    #取得商品內容
    for item, thename in zip(driver.find_elements(by=By.XPATH, value='//*[@data-sqe="link"]'), driver.find_elements(by=By.XPATH, value='//*[@data-sqe="name"]')):
        #商品ID、商家ID
        getID = item.get_attribute('href')
        theitemid = int((getID[getID.rfind('.')+1:getID.rfind('?')]))
        theshopid = int(getID[ getID[:getID.rfind('.')].rfind('.')+1 :getID.rfind('.')]) 
        itemid.append(theitemid)
        shopid.append(theshopid)
        
        #商品名稱
        getname = thename.text.split('\n')[0]
        print('抓取： '+getname)
        name.append(getname)
        
        #價格
        thecontent = item.text
        thecontent = thecontent[(thecontent.find(getname)) + len(getname):]
        thecontent = thecontent.replace('萬','000')
        thecut = thecontent.split('\n')

        if bool(re.search('市|區|縣|鄉|海外|中國大陸', thecontent)): #有時會沒有商品地點資料
            if bool(re.search('已售出', thecontent)): #有時會沒銷售資料
                if '出售' in thecut[-3][1:]:
                    theprice = thecut[-4][1:]
                else:
                    theprice = thecut[-3][1:]

            else:
                theprice = thecut[-2][1:]
        else:
            if re.search('已售出', thecontent): #有時會沒銷售資料
                theprice = thecut[-2][1:]
            else:
                theprice = thecut[-1][1:]
                
        theprice = theprice.replace('$','')
        theprice = theprice.replace(',','')
        theprice = theprice.replace('售','')
        theprice = theprice.replace('出','')
        theprice = theprice.replace(' ','')
        if ' - ' in theprice:
            theprice = (int(theprice.split(' - ')[0]) +int(theprice.split(' - ')[1]))/2
        if '-' in theprice:
            theprice = (int(theprice.split('-')[0]) +int(theprice.split('-')[1]))/2
        price.append(int(theprice))
        
        #請求商品詳細資料
        itemDetail = goods_detail(item_id = theitemid, shop_id = theshopid)['data']
        
        brand.append(itemDetail['brand']) #品牌
        stock.append(itemDetail['stock']) #存貨數量
        ctime.append(itemDetail['ctime']) #上架時間
        description.append(itemDetail['description']) #商品文案
        discount.append(itemDetail['discount']) #折數
        can_use_bundle_deal.append(itemDetail['can_use_bundle_deal']) #可否搭配購買
        can_use_wholesale.append(itemDetail['can_use_wholesale']) #可否大量批貨購買
        tier_variations.append(itemDetail['tier_variations']) #選項
        historical_sold.append(itemDetail['historical_sold']) #歷史銷售量
        is_cc_installment_payment_eligible.append(itemDetail['is_cc_installment_payment_eligible']) #可否分期付款
        is_official_shop.append(itemDetail['is_official_shop']) #是否官方賣家帳號
        is_pre_order.append(itemDetail['is_pre_order']) #是否可預購
        liked_count.append(itemDetail['liked_count']) #喜愛數量
        
        #SKU
        all_sku=[]
        for sk in itemDetail['models']:
            all_sku.append(sk['name'])
        SKU.append(all_sku) #SKU
        shop_location.append(itemDetail['shop_location']) #商家地點
        cmt_count.append(itemDetail['cmt_count']) #評價數量
        five_star.append( itemDetail['item_rating']['rating_count'][5] ) #五星
        four_star.append( itemDetail['item_rating']['rating_count'][4] ) #四星
        three_star.append( itemDetail['item_rating']['rating_count'][3] ) #三星
        two_star.append( itemDetail['item_rating']['rating_count'][2] ) #二星
        one_star.append( itemDetail['item_rating']['rating_count'][1] ) #一星
        rating_star.append(itemDetail['item_rating']['rating_star']) #評分
        
        # 消費者評論詳細資料
        iteComment = goods_comments(item_id = theitemid, shop_id = theshopid)
        userid = [] #使用者ID
        anonymous = [] #是否匿名
        commentTime = [] #留言時間
        is_hidden = [] #是否隱藏
        orderid = [] #訂單編號
        comment_rating_star = [] #給星
        comment = [] #留言內容
        product_SKU = [] #商品規格
        
        for comm in iteComment:
            userid.append(comm['userid'])
            anonymous.append(comm['anonymous'])
            commentTime.append(comm['ctime'])
            is_hidden.append(comm['is_hidden'])
            orderid.append(comm['orderid'])
            comment_rating_star.append(comm['rating_star'])
            try:
                comment.append(comm['comment'])
            except:
                comment.append(None)
            
            p=[]
            for pro in comm['product_items']:
                try:
                    p.append(pro['model_name'])
                except:
                    p.append(None)
                    
            product_SKU.append(p)
            
        commDic = {
            '商品ID':[ theitemid for x in range(len(iteComment)) ],
            '賣家ID':[ theshopid for x in range(len(iteComment)) ],
            '商品名稱':[ getname for x in range(len(iteComment)) ],
            '價格':[ int(theprice) for x in range(len(iteComment)) ],
            '使用者ID':userid,
            '是否匿名':anonymous,
            '留言時間':commentTime,
            '是否隱藏':is_hidden,
            '訂單編號':orderid,
            '給星':comment_rating_star,
            '留言內容':comment,
            '商品規格':product_SKU
            }

        container_comment = pd.concat([container_comment,pd.DataFrame(commDic)], axis=0)
        
    dic = {
            '商品ID':itemid,
            '賣家ID':shopid,
            '商品名稱':name,
            '品牌':brand,
            '存貨數量':stock,
            '價格':price,
            '商品文案':description,
            '折數':discount,
            '可否搭配購買':can_use_bundle_deal,
            '可否大量批貨購買':can_use_wholesale,
            '選項':tier_variations,
            '歷史銷售量':historical_sold,
            '可否分期付款':is_cc_installment_payment_eligible,
            '是否官方賣家帳號':is_official_shop,
            '是否可預購':is_pre_order,
            '喜愛數量':liked_count,
            '商家地點':shop_location,
            'SKU':SKU,
            '評價數量':cmt_count,
            '五星':five_star,
            '四星':four_star,
            '三星':three_star,
            '二星':two_star,
            '一星':one_star,
            '評分':rating_star,
            }

    #資料整合
    container_product = pd.concat([container_product,pd.DataFrame(dic)], axis=0)
    #暫時存檔紀錄
    container_product.to_csv('shopeeAPIData'+str(i+1)+'_Product.csv', encoding = ecode)
    container_comment.to_csv('shopeeAPIData'+str(i+1)+'_Comment.csv', encoding = ecode)

    print('目前累積商品： ' + str(len(container_product)) + ' 留言累積' + str(len(container_comment)))
    time.sleep(random.randint(5,10))

container_product.to_csv(keyword +'_商品資料.csv', encoding = ecode, index=False)
container_comment.to_csv(keyword +'_留言資料.csv', encoding = ecode, index=False)

tEnd = time.time()#計時結束
totalTime = int(tEnd - tStart)
minute = totalTime // 60
second = totalTime % 60
print('資料儲存完成，花費時間（約）： ' + str(minute) + ' 分 ' + str(second) + '秒')
