# -*- coding: utf-8 -*-
"""
Created on Sat May 22 21:27:55 2021

@author: Ivan
課程教材：行銷人轉職爬蟲王實戰｜5大社群平台＋2大電商
版權屬於「楊超霆」所有，若有疑問，可聯絡ivanyang0606@gmail.com

第六章 Youtube中尋找KOL夥伴
Youtube爬蟲－社群資料
"""
# selenium，2022/9/17 將套件更新到4.4.3版本，因此寫法全部都更新過
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
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
            time.sleep(2)
            driver.execute_script('window.scrollBy(0,4000)')
            time.sleep(1)
            element = driver.find_elements_by_xpath(xpathText) # 抓取指定的標籤
            if len(element) > remenber: # 檢查滾動後的數量有無增加
                remenber = len(element)
            else:
                doit = False # 還是無增加，停止滾動
        time.sleep(1)
    return element #回傳元素內容


# 自動下載ChromeDriver
service = ChromeService(executable_path=ChromeDriverManager().install())

# 關閉通知提醒
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

# 開啟瀏覽器
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
time.sleep(5)

#抓取Youtuber_頻道資料.csv
getdata = pd.read_csv('Youtuber_頻道資料.csv', encoding = 'utf-8-sig')

#準備容器
youtuberChannel = []
channelLink = []
articleLink = []
articleContent = []
postTime = []
good = []
commentNum = []
comment = []
# 開始一個一個爬蟲
for yName, yChannel in zip(getdata['Youtuber頻道名稱'], getdata['頻道網址']):
    #到社群頁面
    driver.get(str(yChannel) + '/community')
    time.sleep(10)
    
    # 滾動頁面
    getAll_url = scroll(driver, '//yt-formatted-string[@id="published-time-text"]/a')
        
    # 文章網址必須先擷取出來
    for article in getAll_url:
        articleLink.append(article.get_attribute('href')) # 取得文章連結
        postTime.append(article.text) # 取得發文時間
        youtuberChannel.append(yName)
        channelLink.append(yChannel)
    print('頻道'+ str(yName) + '共有'+ str(len(articleLink)) + '篇文章，開始抓取文章內容')
    
    for goto_url in tqdm(articleLink):
        
        # 去到該文章
        driver.get(goto_url)
        time.sleep(3)
        
        articleContent.append(driver.find_element(by=By.ID, value='expander').text) # 取得文章內文
        good.append(driver.find_element(by=By.ID, value='vote-count-middle').text) # 取得文章讚數
        time.sleep(3)
        
        # 取得留言總數量
        getcommentNum = int(driver.find_element(by=By.XPATH, value='//h2[@id="count"]/yt-formatted-string/span').text)
        commentNum.append(getcommentNum)
        time.sleep(3)
        
        #--- 開始進行「取得留言」工程
        # 滾動頁面
        getcomment = scroll(driver, '//div[@id="main"]')
        getfans = driver.find_elements(by=By.ID, value='author-text') # 發言者
            
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
        
        comment.append(containar) # 儲存所有留言
        
    # 暫存器
    dic = {
       'Youtuber頻道名稱' : youtuberChannel,
       '頻道網址' : channelLink,
       '文章連結' : articleLink,
        '文章內容' : articleContent,
        '發文時間' : postTime,
        '讚數' : good,
        '留言數量' : commentNum,
        '留言' : comment
       }
    pd.DataFrame(dic).to_csv(str(yName)+'_Youtuber_社群資料.csv', 
                             encoding = 'utf-8-sig', 
                             index=False)

    print('頻道 '+str(yName)+' 爬取完成')
    
dic = {
       'Youtuber頻道名稱' : youtuberChannel,
       '頻道網址' : channelLink,
       '文章連結' : articleLink,
        '文章內容' : articleContent,
        '發文時間' : postTime,
        '讚數' : good,
        '留言數量' : commentNum,
        '留言' : comment
       }
pd.DataFrame(dic).to_csv('Youtuber_社群資料.csv', 
                         encoding = 'utf-8-sig', 
                         index=False)
