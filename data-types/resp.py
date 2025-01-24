import requests

response = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest")
print(response)

data = response.json()
print(data)

