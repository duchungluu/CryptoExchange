import json
import requests

global_url="https://api.coinmarketcap.com/v2/global/"

request = requests.get(global_url)

print (request)
results = request.json()

print(json.dumps(results, sort_keys=True, indent =4))