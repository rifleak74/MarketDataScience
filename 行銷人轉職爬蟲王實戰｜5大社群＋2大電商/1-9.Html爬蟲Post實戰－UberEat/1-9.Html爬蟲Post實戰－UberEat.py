# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 17:40:25 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第一章 爬蟲基本訓練
Html爬蟲Post實戰－UberEat
"""
import requests
import json
# 要抓取的網址
url = 'https://www.ubereats.com/api/getFeedV1?localeCode=tw'
# 請求附帶的資料
post_head = {
# 'accept': '*/*',
# 'accept-encoding': 'gzip, deflate, br',
# 'accept-language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
# 'content-length': '911',
# 'content-type': 'application/json',
'cookie': 'dId=4815da68-ec54-41d4-9717-2978d469ccc4; marketing_vistor_id=8d8159b6-8ae7-4040-8ce8-431f796768ae; uev2.gg=true; CONSENTMGR=c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1619508195182%7Cconsent:true; _gcl_au=1.1.1907720607.1619508195; _ga=GA1.2.143653121.1619508195; _rdt_uuid=1619508195433.3e919407-6169-4bda-a5c8-d715308fac04; _scid=47885b85-ba6f-4c2e-9907-bd73058b06af; _fbp=fb.1.1619508195791.195714405; _hjid=67222cd2-0078-48ad-9bc2-41d526e267d9; _sctr=1|1619452800000; utag_main=v_id:01791235ef4d0021aedf6e028b4803072001b06a007e8$_sn:3$_se:7$_ss:0$_st:1619692859744$ses_id:1619691041827%3Bexp-session$_pn:1%3Bexp-session; _uetvid=6ee13850a72911eb840fdb3574449f51; uev2.id.xp=b4301128-edc5-4921-9931-156da447811b; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2MjA2OTU2NjQsImV4cCI6MTYyMDc4MjA2NH0.-LHdA1q-4ZoAjngSy__de90ENyja1m_4WqcipFQtGvc; uev2.id.session=9480d0df-34dc-4563-9975-8c11d960fd3d; uev2.ts.session=1620734387177; uev2.loc=%7B%22address%22%3A%7B%22address1%22%3A%22%E5%BB%BA%E5%9C%8B%E5%8C%97%E8%B7%AF%E4%B8%80%E6%AE%B522%E8%99%9F%22%2C%22address2%22%3A%22%E5%8F%B0%E5%8C%97%E5%B8%82%E4%B8%AD%E5%B1%B1%E5%8D%80%22%2C%22aptOrSuite%22%3A%22%22%2C%22eaterFormattedAddress%22%3A%2210491%E5%8F%B0%E7%81%A3%E5%8F%B0%E5%8C%97%E5%B8%82%E4%B8%AD%E5%B1%B1%E5%8D%80%E5%BB%BA%E5%9C%8B%E5%8C%97%E8%B7%AF%E4%B8%80%E6%AE%B522%E8%99%9F%22%2C%22subtitle%22%3A%22%E5%8F%B0%E5%8C%97%E5%B8%82%E4%B8%AD%E5%B1%B1%E5%8D%80%22%2C%22title%22%3A%22%E5%BB%BA%E5%9C%8B%E5%8C%97%E8%B7%AF%E4%B8%80%E6%AE%B522%E8%99%9F%22%2C%22uuid%22%3A%22%22%7D%2C%22latitude%22%3A25.0468611%2C%22longitude%22%3A121.536426%2C%22reference%22%3A%22ElROby4gMjIsIFNlY3Rpb24gMSwgSmlhbmd1byBOb3J0aCBSb2FkLCBaaG9uZ3NoYW4gRGlzdHJpY3QsIFRhaXBlaSBDaXR5LCBUYWl3YW4gMTA0OTEiUBJOCjQKMgnTd-16YqlCNBFA_oaSx85XOhoeCxDuwe6hARoUChIJm2wtXvmrQjQRdcece4f6Gs4MEBYqFAoSCSsfxP5hqUI0EQx_kdQ4ReST%22%2C%22referenceType%22%3A%22google_places%22%2C%22type%22%3A%22google_places%22%2C%22source%22%3A%22manual_auto_complete%22%2C%22addressComponents%22%3A%7B%22countryCode%22%3A%22TW%22%2C%22firstLevelSubdivisionCode%22%3A%22%E5%8F%B0%E5%8C%97%E5%B8%82%22%2C%22city%22%3A%22%E4%B8%AD%E5%B1%B1%E5%8D%80%22%2C%22postalCode%22%3A%2210491%22%7D%2C%22originType%22%3A%22user_autocomplete%22%7D',
# 'dnt': '1',
# 'origin': 'https://www.ubereats.com',
# 'referer': 'https://www.ubereats.com/tw/feed?pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFNSVCQiVCQSVFNSU5QyU4QiVFNSU4QyU5NyVFOCVCNyVBRiVFNCVCOCU4MCVFNiVBRSVCNTIyJUU4JTk5JTlGJTIyJTJDJTIycmVmZXJlbmNlJTIyJTNBJTIyRWxST2J5NGdNaklzSUZObFkzUnBiMjRnTVN3Z1NtbGhibWQxYnlCT2IzSjBhQ0JTYjJGa0xDQmFhRzl1WjNOb1lXNGdSR2x6ZEhKcFkzUXNJRlJoYVhCbGFTQkRhWFI1TENCVVlXbDNZVzRnTVRBME9URWlVQkpPQ2pRS01nblRkLTE2WXFsQ05CRkFfb2FTeDg1WE9ob2VDeER1d2U2aEFSb1VDaElKbTJ3dFh2bXJRalFSZGNlY2U0ZjZHczRNRUJZcUZBb1NDU3NmeFA1aHFVSTBFUXhfa2RRNFJlU1QlMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBMjUuMDQ2ODYxMSUyQyUyMmxvbmdpdHVkZSUyMiUzQTEyMS41MzY0MjYlN0Q%3D',
# 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
# 'sec-ch-ua-mobile': '?0',
# 'sec-fetch-dest': 'empty',
# 'sec-fetch-mode': 'cors',
# 'sec-fetch-site': 'same-origin',
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
'x-csrf-token': 'x',
# 'x-uber-xps': '%7B%22eats_web_promo_page%22%3A%7B%22name%22%3A%22treatment%22%7D%2C%22eats_web_ssr_base_store_v2%22%3A%7B%22name%22%3A%22control%22%7D%2C%22eats_web_hybrid_pickup_map_phase_1%22%3A%7B%22name%22%3A%22treatment%22%7D%2C%22eats_web_cro_store_back_button%22%3A%7B%22name%22%3A%22control2%22%7D%2C%22eats_web_cro_store_persistent_food_image%22%3A%7B%22name%22%3A%22t_persist_image%22%7D%2C%22web_eats_dietary_tags%22%3A%7B%22name%22%3A%22treatment%22%7D%2C%22eats_web_coi_checkout_v2%22%3A%7B%22name%22%3A%22treatment%22%7D%2C%22eats_web_cro_mweb_app_upsell_v2%22%3A%7B%22name%22%3A%22t_half_eater_link%22%7D%2C%22eats_web_r2e_invoice%22%3A%7B%22name%22%3A%22treatment%22%7D%2C%22eats_web_hybrid_pickup_map_phase_2%22%3A%7B%22name%22%3A%22treatment%22%7D%2C%22eats_web_cro_hp_removed_carousels%22%3A%7B%22name%22%3A%22t_carousels_removed%22%7D%2C%22eats_web_cro_mweb_signin_universal%22%3A%7B%22name%22%3A%22control2%22%7D%7D'
        }

post_data = {
# 'billboardUuid': "",
'cacheKey': "JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFNSVCQiVCQSVFNSU5QyU4QiVFNSU4QyU5NyVFOCVCNyVBRiVFNCVCOCU4MCVFNiVBRSVCNTIyJUU4JTk5JTlGJTIyJTJDJTIycmVmZXJlbmNlJTIyJTNBJTIyRWxST2J5NGdNaklzSUZObFkzUnBiMjRnTVN3Z1NtbGhibWQxYnlCT2IzSjBhQ0JTYjJGa0xDQmFhRzl1WjNOb1lXNGdSR2x6ZEhKcFkzUXNJRlJoYVhCbGFTQkRhWFI1TENCVVlXbDNZVzRnTVRBME9URWlVQkpPQ2pRS01nblRkLTE2WXFsQ05CRkFfb2FTeDg1WE9ob2VDeER1d2U2aEFSb1VDaElKbTJ3dFh2bXJRalFSZGNlY2U0ZjZHczRNRUJZcUZBb1NDU3NmeFA1aHFVSTBFUXhfa2RRNFJlU1QlMjIlMkMlMjJyZWZlcmVuY2VUeXBlJTIyJTNBJTIyZ29vZ2xlX3BsYWNlcyUyMiUyQyUyMmxhdGl0dWRlJTIyJTNBMjUuMDQ2ODYxMSUyQyUyMmxvbmdpdHVkZSUyMiUzQTEyMS41MzY0MjYlN0Q=/DELIVERY///0/0//JTVCJTVE///",
# 'carouselId': "",
# 'date': "",
# 'endTime': '0',
# 'feedProvider': "",
# 'feedSessionCount': {'announcementCount': '0', 'announcementLabel': ""},
# 'getFeedItemType': "PINNED",
# 'marketingFeedType': "",
# 'showSearchNoAddress': False,
# 'sortAndFilters': [],
# 'startTime': '0',
# 'userQuery': ""
    }

#請求網站
list_req = requests.post(url, 
                         headers = post_head,
                         data = post_data)
getdata = json.loads(list_req.content)
