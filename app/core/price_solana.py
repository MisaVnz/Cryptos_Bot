from typing import Optional
import requests
import json

def obtener_precio_solana() -> Optional[float]:
    """Obtiene el precio actual de Solana en USD desde CoinGecko."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP no exitosos
        data = response.json()
        precio_sol = data['solana']['usd']
        return precio_sol
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el precio: {e}")
        return None

if __name__ == "__main__":
    precio = obtener_precio_solana()
    if precio:
        print(f"El precio actual de Solana (SOL) en USD es: {precio}")