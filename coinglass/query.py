import os
import io
from os.path import join, dirname
import requests
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_key = os.environ.get("API_KEY")

base_url= "https://open-api.coinglass.com"
api_endpoint = "/public/v2/open_interest_history"

symbol = "BTC" 
currency = "USD"
time_type = "all" # m1, m5, m15, h1, h4, h12, all

url = base_url + api_endpoint + "?symbol=" + symbol + "&currency=" + currency + "&time_type=" + time_type

headers = {"accept": "application/json", "coinglassSecret": api_key}
response = requests.get(url, headers=headers).json()

rawData = response["data"]

local_dict = {}
for key, value in rawData.items():
    if type(value) is dict:
        for k, v in value.items():
            if k == "Binance":
                local_dict[k] = v
    else:
        local_dict[key] = value

pdframe = pd.DataFrame(local_dict)
pdframe["dateList"]=[datetime.fromtimestamp(x).strftime("%x %X") for x in pdframe["dateList"].values/1000]
pdframe.to_csv("BTC_USDT_Binance.csv", sep=',')

# print(pdframe)