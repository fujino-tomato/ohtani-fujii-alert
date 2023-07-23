import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://shogi-sanpo.com/fujiisouta/result/"
res = requests.get(url)
res.encoding = "utf-8"

soup = BeautifulSoup(res.text, "html.parser")
elems = soup.select("#mainArea > div:nth-child(21) > div > ul > li")

# ラベルの作成
elem = elems[0]
label = []
for div in elem.find_all("div"):
    label.append(div.text)
df = pd.DataFrame(columns=label)

# 中身のデータの追加
for i in range(1, 6):
    print(i)
    data = []
    for div in elems[i].find_all("div"):
        print(div.text)
        data.append(div.text)
    df.loc[i-1] = data

print(df)