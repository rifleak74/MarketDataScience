# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:18:31 2020

@author: Ivan
"""
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "自閉式寄件"  #郵件標題
content["from"] = "ivanyang0606@gmail.com"  #寄件者
content["to"] = "aaaaaa111111aaaaaa1111ox@gmail.com" #收件者
content.attach(
                MIMEText("""
                        親愛的 <u>Ivan</u>您好：<br><br>
                        
                        您寫這篇文章真是辛苦了，<b>不如您自己追蹤自己吧！</b> <br>
                        趕快手刀點擊<a href="https://medium.com/@ivanyang0606">Ivan的Medium文章</a>。
                        
                        """
                        , "html"))  #郵件內容


with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("ivanyang0606@gmail.com", "cvztwtflzkntbuql")  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件
        print("成功傳送")
    except Exception as e:
        print("Error message: ", e)