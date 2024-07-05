import json
import requests
import sys

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
price = response.json()
# print(json.dumps(price, indent=2))
price_usd = price["bpi"]["USD"]["rate_float"]
user_price = float(price_usd) * float(sys.argv[1])
print(f"${user_price:,.4f}")