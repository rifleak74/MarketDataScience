# -*- coding: utf-8 -*-
"""
Created on Sat May 22 23:28:54 2021
@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com
第六章 Youtube中尋找KOL夥伴
Youtube爬蟲－影片資料
"""
# selenium
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
import pandas as pd
import time
import random
from datetime import datetime
from tqdm import tqdm

# 滾動頁面
def scroll(driver, xpathText):
    remenber = 0
    doit = True
    while doit:
        driver.execute_script('window.scrollBy(0,4000)')
        time.sleep(1)
        element = driver.find_elements_by_xpath(xpathText) # 抓取指定的標籤
        if len(element) > remenber: # 檢查滾動後的數量有無增加
            remenber = len(element)
        else: # 沒增加則等待一下，然後在滾動一次
            time.sleep(random.randint(5,20))
            driver.execute_script('window.scrollBy(0,4000)')
            time.sleep(3)
            element = driver.find_elements_by_xpath(xpathText) # 抓取指定的標籤
            if len(element) > remenber: # 檢查滾動後的數量有無增加
                remenber = len(element)
            else:
                doit = False # 還是無增加，停止滾動
        time.sleep(2)
    return element #回傳元素內容

# 設定基本參數
desired_capabilities = DesiredCapabilities.PHANTOMJS.copy()
#此處必須換成自己電腦的User-Agent
desired_capabilities['phantomjs.page.customHeaders.User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
# PhantomJS driver 路徑 似乎只能絕對路徑
driver = webdriver.PhantomJS(executable_path = 'phantomjs', desired_capabilities=desired_capabilities)
# 關閉通知提醒
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
# 開啟瀏覽器
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
time.sleep(5)

#抓取csv資料
getdata = pd.read_csv('Youtuber_頻道資料.csv', encoding = 'utf-8-sig')

#準備容器
youtuberChannel = []
channelLink = []
videoName = []
videoLink = []
good = []
looking = []
videoDate = []
videoContent = []
commentNum = []
comment = []
for yName, yChannel, allLink in zip(getdata['Youtuber頻道名稱'], getdata['頻道網址'], getdata['所有影片連結']):
    print('開始爬取 '+ yName +' 的影片')
    for link in tqdm(eval(allLink)):
        # 去到該影片
        driver.get(link)
        
        while len(driver.find_elements_by_xpath('//h1[@class="style-scope ytd-watch-metadata"]')) == 0:
            time.sleep(5)
        
        youtuberChannel.append(yName) # 取得Youtuber頻道名稱
        channelLink.append(yChannel) # 取得頻道網址
        videoLink.append(allLink) # 取得影片連結
        # 取得影片名稱
        getvideoName = driver.find_element_by_xpath('//h1[@class="style-scope ytd-watch-metadata"]').text
        print('開始爬取： '+ getvideoName)
        videoName.append(getvideoName)
        # 取得讚數
        getgood = driver.find_element_by_xpath('//div[@id="menu-container"]/div/ytd-menu-renderer/div[1]/ytd-toggle-button-renderer[1]/a/yt-formatted-string').get_attribute('aria-label')
        if '尚未有人表示喜歡' in getgood:
            good.append(0) 
        else:
            getgood = getgood.replace(' 人喜歡','')
            getgood = getgood.replace(',','')
            good.append(getgood) 
        # 觀看數、影片時間
        getlook = driver.find_element_by_id('formatted-snippet-text').text
        getlook = getlook.split('日 ')[0]

        getlook = getlook.replace('觀看次數：','')
        getlook = getlook.replace(' ','')
        getlook = getlook.replace('.','')
        getlook = getlook.replace(',','')
        getlook = getlook.split('次')
        videoDate.append(datetime.strptime(getlook[1], "%Y年%m月%d")) # 取得影片時間
        
        looking.append(int(getlook[0])) # 取得觀看數
        time.sleep(random.randint(2,5))
        
        # 點擊更多內容
        driver.find_element_by_id('expand').click()
        time.sleep(random.randint(2,5))
        getContent = driver.find_element_by_xpath('//yt-formatted-string[@class="style-scope ytd-text-inline-expander"]').text
        videoContent.append(getContent.split('日 ')[1]) # 取得影片介紹
        
        # 先滾動一小段在取得留言數
        while len(driver.find_elements_by_xpath('//h2[@id="count"]/yt-formatted-string/span'))==0:
            driver.execute_script('window.scrollBy(0,'+str(random.randint(30,50))+')')
            time.sleep(random.randint(2,5))

        getcommentNum = driver.find_element_by_xpath('//h2[@id="count"]/yt-formatted-string/span').text
        getcommentNum = getcommentNum.replace(',','')
        commentNum.append(int(getcommentNum)) # 取得留言數
        
        #--- 開始進行「取得留言」工程
        # 滾動頁面
        getcomment = scroll(driver, '//div[@id="main"]')
        getfans = driver.find_elements_by_id('author-text') # 發言者
        
        # 儲存留言內容
        commentMan = []
        manChannel = []
        post_time = []
        comment_content = []
        comment_good = []
        
        count = 0 # 用來編號留言
        containar = {}
        for fans, com in zip(getfans, getcomment):
            if count != 0: # 第一次不需要執行，因為是youter自己的資料
                getcom = com.text
                getcom = getcom.replace('\n回覆','')
                getcom = getcom.replace('\nREPLY','')
                cutcom = getcom.split('\n')
                
                if len(cutcom) == 3: # 若沒有人按讚，則補0
                    cutcom.append(0)
                try:
                    containar['留言'+str(count)] = {
                        '發言者':cutcom[0],
                        '發言者頻道': fans.get_attribute('href'),
                        '發言時間':cutcom[1],
                        '發言內容':cutcom[2],
                        '讚數':cutcom[3]
                        }
                except:# 碰到異常資料之極端處理
                    containar['留言'+str(count)] = {'資料異常'}
            count = count + 1
        
        comment.append(containar) # 取得留言
        
    # 暫存器
    dic = {
           'Youtuber頻道名稱' : youtuberChannel,
            '頻道網址' : channelLink,
            '影片名稱' : videoName,
            '影片連結' : videoLink,
            '影片發布時間' : videoDate,
            '讚數' : good,
            '觀看次數' : looking,
            '影片文案內容' : videoContent,
            
            '留言數量' : commentNum,
            '留言' : comment
           }
    pd.DataFrame(dic).to_csv(str(yChannel)+'_Youtuber_影片資料.csv', 
                             encoding = 'utf-8-sig', 
                             index=False)
    
    print('頻道 '+str(yChannel)+' 爬取完成')
    
dic = {
       'Youtuber頻道名稱' : youtuberChannel,
        '頻道網址' : channelLink,
        '影片名稱' : videoName,
        '影片連結' : videoLink,
        '影片發布時間' : videoDate,
        '讚數' : good,
        '觀看次數' : looking,
        '影片文案內容' : videoContent,
        
        '留言數量' : commentNum,
        '留言' : comment
       }
pd.DataFrame(dic).to_csv('Youtuber_影片資料.csv', 
                         encoding = 'utf-8-sig', 
                         index=False)