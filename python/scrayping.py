import pandas as pd
import requests
from bs4 import BeautifulSoup


def fujii_scrayping():
    url = "https://www.shogi.or.jp/player/pro/307.html"
    res = requests.get(url)
    res.encoding = "utf-8"

    soup = BeautifulSoup(res.text, "html.parser")
    elems = soup.select("#contents > div.sp_player_matchresult > div > table > tbody")
    elem = elems[0]

    # ラベルの作成
    label = []
    for tb_col in elem.find_all("th"):
        label.append(tb_col.text)

    # 中身のデータの追加
    data = []
    for data_ind in elem.find_all("tr"):
        d = {}
        for i, data_col in enumerate(data_ind.find_all("td")):
            d[label[i]] = data_col.text
        data.append(d)
    df = pd.DataFrame(data, columns=label, index=None)
    return df


# df.to_csv("../fujii.csv")
