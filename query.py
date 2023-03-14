import os
import pandas as pd
from datetime import datetime
from os.path import join, dirname
from binance.client import Client
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("SECRET_KEY")
client=Client(api_key,api_secret)

interest = client.futures_open_interest_hist(symbol='BTCUSDT', period='15m')
df=pd.DataFrame(interest)
df=df.set_index("timestamp")
df["sumOpenInterest"]=df["sumOpenInterest"].astype("float")
df["sumOpenInterestValue"]=df["sumOpenInterestValue"].astype("float")
# df.index=datetime.utcfromtimestamp(df.index.values).strftime('%Y-%m-%d %H:%M:%S')
print(df)