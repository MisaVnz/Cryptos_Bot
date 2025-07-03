from typing import Optional
import requests
import json

def obtener_precio_bitcoin() -> Optional[float]:
    """Obtiene el precio actual de BNB en USD desde CoinGecko."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP no exitosos
        data = response.json()
        precio_bitcoin = data['bitcoin']['usd']
        return precio_bitcoin
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el precio: {e}")
        return None

if __name__ == "__main__":
    precio = obtener_precio_bitcoin()
    if precio:
        print(f"El precio actual del Bitcoin (BTC) en USD es: {precio}")