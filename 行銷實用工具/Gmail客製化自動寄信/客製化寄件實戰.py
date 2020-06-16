# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:18:31 2020

@author: Ivan
"""
import pandas as pd
import smtplib
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 
custemor = pd.read_csv('顧客訂單.csv')

sendFrom = "寄件者信箱"  #寄件者
senderPassword = "寄件者密碼"

#寄送檔案專用
def sendFile(fileName, content):
    pdfload = MIMEApplication(open(fileName,'rb').read()) 
    pdfload.add_header('Content-Disposition', 
                       'attachment', 
                       filename=fileName) 
    content.attach(pdfload) 
    return content

#開始每一筆資料進去客製化的寄送信件
for coste in custemor:
    message=''
    #先確認性別，決定給予什麼稱謂
    if coste['性別'] == '男':
        gender='先生'
    else:
        gender='小姐'
        
    # 整理將要傳送出去的文字
    message += '親愛的 {} {}您好：\n\n非常感謝您在本店購買「{}」{}個，共 {}元。\n\nIvan股份有限公司\nMediemJ文章：https://medium.com/@ivanyang0606'.format(
                    coste['姓名'], 
                    gender,
                    coste['購買商品'],
                    coste['數量'],
                    coste['購買總金額'],
                    )

    content = MIMEMultipart()  #建立MIMEMultipart物件
    content["subject"] = "Ivan網路平台感謝您的光顧"  #郵件標題
    content["from"] = sendFrom
    content["to"] = coste['電子郵件'] #收件者
    content.attach(MIMEText(message))  #郵件內容
    
    #以下為檔案附件，若要客製化寄送不同的附件，可以用if來達成
    content.attach(MIMEImage(Path("夕陽.jpg").read_bytes()))  # 郵件圖片內容
    for file in ['test.pdf','test.docx','顧客訂單.csv']: #把想寄送的黨名直接放在陣列，讓程式自動去抓取
        content = sendFile(file, content)
    
    
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login(sendFrom, senderPassword)  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("成功傳送")
        except Exception as e:
            print("Error message: ", e)
