from typing import Optional
import requests
import json

from app.app_logger import get_logger
from app.settings import Config

logger = get_logger(f"[{Config().APP_NAME}: Core Module]")

def obtener_precio_tron() -> Optional[float]:
    """Obtiene el precio actual de TRON en USD desde CoinGecko."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=tron&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP no exitosos
        data = response.json()
        precio_tron = data['tron']['usd']
        return precio_tron
    except requests.exceptions.RequestException as e:
        logger.error(f"Error al obtener el precio: {e}")
        return None

if __name__ == "__main__":
    precio = obtener_precio_tron()
    if precio:
        print(f"El precio actual de TRON (TRX) en USD es: {precio}")