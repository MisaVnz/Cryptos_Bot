from typing import Optional
import requests
import json

def obtener_precio_ethereum() -> Optional[float]:
    """Obtiene el precio actual de Ethereum en USD desde CoinGecko."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP no exitosos
        data = response.json()
        precio_eth = data['ethereum']['usd']
        return precio_eth
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el precio: {e}")
        return None

if __name__ == "__main__":
    precio = obtener_precio_ethereum()
    if precio:
        print(f"El precio actual de Ethereum (ETH) en USD es: {precio}")