from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
text= '想與姊妹掏來個下午茶談天時光，應該不少人都會想到咖啡廳聚集地 - 捷運中山站，除了幾間著名大家耳熟能詳的咖啡'
（因為過多，詳情請看github程式碼，以下省略...）
def emotion(thetext):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='你的憑證檔案名稱.json'
    # 實例化一個客戶端
    client = language.LanguageServiceClient()
    # 要分析的文本
    text = thetext
    document = types.Document(
                                content=text,
                                type=enums.Document.Type.PLAIN_TEXT)
    # 檢測文本的情緒
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    return([sentiment.score, sentiment.magnitude])

get =emotion(text)



