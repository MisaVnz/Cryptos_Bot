import requests

url = "https://api.coingecko.com/api/v3/simple/price"
params = {  
         "ids": "bitcoin",
         "vs_currencies": "USD"
}

 
headers = { 'x-cg-demo-api-key': "CG-oKSSdgGzgeqrRAckMFotYJyK" }

response = requests.get(url, params = params)

if response.status_code == 200:
         data = response.json()
         Bitcoin_price = data["bitcoin"]["usd"]
         print(f"El precio del Bitcoin en USD es ${Bitcoin_price}")
else:
        print("Falla al recibir informacion de la API")