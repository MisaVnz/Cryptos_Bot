import requests
from bs4 import BeautifulSoup
import os

# Configuración
URL = "https://www.futbolred.com/partidos/copa-libertadores"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
OUTPUT_FILE = "copa_libertadores.html"

def scrape_and_save_html():
    try:
        # 1. Realizar la petición HTTP
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()  # Verifica errores (ej: 404, 403)
        
        # 2. Guardar el HTML en un archivo
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"✅ HTML guardado en: {os.path.abspath(OUTPUT_FILE)}")
        
        # 3. (Opcional) Parsear con BeautifulSoup para extraer datos específicos
        soup = BeautifulSoup(response.text, "html.parser")
        partidos = soup.find_all("div", class_="match-card")  # Ajusta este selector según la página
        
        if partidos:
            print(f"📌 Se encontraron {len(partidos)} partidos.")
        else:
            print("⚠️ No se encontraron partidos. Revisa los selectores.")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    scrape_and_save_html()