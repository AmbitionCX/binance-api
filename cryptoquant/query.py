import requests

URL="https://api.cryptoquant.com/v1/btc/market-data/open-interest?window=day&from=20191001&exchange=bitmex"

headers = {'Authorization': 'Bearer ' + access_token}
response = requests.get(URL, headers=headers)