import requests
import scrape

print("test")

date, title = scrape.kinro()
message = '\n' + date + '\n' + title


# 発行されたトークン
ACCESS_TOKEN = ""

headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

data = {
    "message": message
}

requests.post(
    "https://notify-api.line.me/api/notify",
    headers=headers,
    data=data,
)
