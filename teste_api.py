import requests

url = "https://api.exchangerate.host/latest?base=USD&symbols=BRL"

response = requests.get(url)
print(response.json())
