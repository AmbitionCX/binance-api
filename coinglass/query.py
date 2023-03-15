import os
from os.path import join, dirname
import requests
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

api_key = os.environ.get("API_KEY")

base_url= "https://open-api.coinglass.com"
api_endpoint = "/public/v2/open_interest_history"

symbol = "BTC" 
currency = "USDT"
time_type = "h12" # m1, m5, m15, h1, h4, h12, all

url = base_url + api_endpoint + "?symbol=" + symbol + "&currency=" + currency + "&time_type=" + time_type

headers = {"accept": "application/json", "coinglassSecret": api_key}
response = requests.get(url, headers=headers)

print(response.json())