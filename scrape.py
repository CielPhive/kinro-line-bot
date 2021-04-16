import requests
from bs4 import BeautifulSoup
import datetime
def kinro():
    html_data = requests.get('https://kinro.ntv.co.jp/lineup/')
    soup = BeautifulSoup(html_data.text, "html.parser")


    #最新の金曜ロードショー放送日、タイトルを取得
    date = soup.find(class_='list').find(class_='date').string
    title = soup.find(class_='list').find(class_='title').string
   


    return date, title