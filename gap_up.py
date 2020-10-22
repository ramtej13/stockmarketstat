import pandas as pd
import numpy as np

lable = ["SYMBOL","OPEN","HIGH","LOW","netinvest", "PREV. CLOSE","LTP","CHNG","%CHNG","VOLUME","VALUE","52Wh","52W","365","30D",]
df = pd.read_csv("data/MW-SECURITIES-IN-F&O-22-Oct-2020.csv",names=lable)
df = df.drop(index=0, axis=0)
df = df.sort_values("SYMBOL",ascending=True)

lable = ["todaySYMBOL","OPEN","HIGH","LOW","netinvest", "PREV. CLOSE","LTP","CHNG","%CHNG","VOLUME","VALUE","52Wh","52W","365","30D",]
df_today = pd.read_csv("data/MW-SECURITIES-IN-F&O-22-Oct-20202.csv",names=lable)
df_today = df_today.drop(index=0, axis=0)
df_today = df_today.sort_values("todaySYMBOL",ascending=True)

dictionary = {}
list = []
for i in range(len(df["SYMBOL"].values)):
    high = float(df["HIGH"].values[i].replace(',',''))
    open = float(df_today["OPEN"].values[i].replace(',',''))
    dictionary[str(df["SYMBOL"].values[i])] = ((open-high)/high)*100
    # dictionary["chnage_percentage"] = (float(df["HIGH"].values[i].replace(',',''))-float(df_today["OPEN"].values[i].replace(',','')))/float(df_today["OPEN"].values[i].replace(',',''))

lol = pd.DataFrame.from_dict(data=dictionary,orient='index',columns=["chnage_percentage"])
print(lol.sort_values("chnage_percentage",ascending=False))








