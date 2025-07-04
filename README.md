# Crytos_Bot 🤖

![Python](https://img.shields.io/badge/Python-3.11%252B-blue?logo=python&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?logo=telegram)
![CoinGecko](https://img.shields.io/badge/CoinGecko-API-yellow)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Code Style](https://img.shields.io/badge/code%2520style-black-000000.svg)

> ⚠️  Importante: Nunca compartas tu token de Telegram. Mantén el archivo .env seguro.

Bot profesional para consultar precios de criptomonedas en tiempo real mediante la API de CoinGecko. Desarrollado por MisaVnz y la tutoria de gabrielbaute.

## 🌟 Características Principales
- Arquitectura modular y escalable
- Sistema de logging completo
- Configuración mediante variables de entorno
- Soporte para 5 criptomonedas principales:
  - Bitcoin (`/BTC`)
  - Ethereum (`/ETH`)
  - Solana (`/SOL`)
  - Binance Coin (`/BNB`)
  - Tron (`/TRX`)
- Mensaje de bienvenida personalizado (`/start`)

## 📋 Requisitos

### 🔧 Requisitos Técnicos

| Componente           | Versión    | Descripción                          |
|----------------------|------------|--------------------------------------|
| Python               | 3.11+      | Entorno de ejecución principal       |
| python-telegram-bot  | 20.0+      | Biblioteca para la API de Telegram   |
| requests             | 2.31+      | Conexión con APIs externas           |
| python-dotenv        | 1.0+       | Manejo de variables de entorno       |

### 🌐 Requisitos de Cuentas

| Servicio  | Descripción                                  | Enlace                      |
|-----------|----------------------------------------------|-----------------------------|
| Telegram  | Necesario para crear el bot y obtener token  | [BotFather](https://t.me/BotFather) |
| CoinGecko | Provee datos de precios (sin API key)        | [CoinGecko API](https://www.coingecko.com/en/api) |

## ⚙️ Instalacion

### 🔑 Configuración del Token de Telegram

#### 1. Obtener tu Token de BotFather
1. Busca **@BotFather** en Telegram
2. Ejecuta el comando `/newbot`
3. Sigue las instrucciones paso a paso:
   - Elige un nombre para tu bot (ej: `MyCryptoBot`)
   - Define un username único (debe terminar en `bot`, ej: `MyCryptoPriceBot`)
4. Al finalizar, recibirás un token con formato: 1234567890:ABCdefGHIJKlmNOPQRstUVWXYz

### 2. Configurar el archivo .env
Crea un archivo llamado **`.env`** en la raíz de tu proyecto con este contenido exacto:

TELEGRAM_BOT_KEY="pega_aquí_tu_token"

> ⚠️  Importante:

  - El archivo debe llamarse exactamente .env (no .env.txt ni otro nombre)
  - Usa comillas dobles alrededor del token
  - No incluyas espacios alrededor del =
  - Guarda el archivo en la misma carpeta donde está run.py

## 🏗️ Arquitectura del Proyecto

cryptos-bot/
├── .env # Configuración sensible
├── run.py # Punto de entrada
├── app/
│ ├── bot/ # Lógica de comandos
│ ├── core/ # Conexión con APIs
│ ├── settings/ # Configuración
│ └── app_logger/ # Sistema de logging
└── logs/ # Registros de actividad

## 📋 Comandos Disponibles

| Comando | Descripción | Ejemplo de Salida |
|---------|-------------|-------------------|
| `/start` | Mensaje de bienvenida con instrucciones | "¡Hola! Soy Cryptos Bot..." |
| `/BTC`   | Obtiene el precio actual de Bitcoin | `💰 BTC: $61,420.50` |
| `/ETH`   | Muestra el valor de Ethereum | `💰 ETH: $3,450.25` |
| `/SOL`   | Consulta el precio de Solana | `💰 SOL: $150.30` |
| `/BNB`   | Proporciona el valor de Binance Coin | `💰 BNB: $550.75` |
| `/TRX`   | Devuelve el precio actual de Tron | `💰 TRX: $0.12` |

## 📚 Documentación

La aplicación consume datos de la [API Pública de CoinGecko](https://www.coingecko.com/en/api/documentation) para obtener los precios de las criptomonedas en tiempo real.

### Uso básico:
1. Abre Telegram y busca tu bot
2. Escribe cualquiera de los comandos anteriores
3. Recibe la información en formato claro con:
   - Emoji identificativo (💰)
   - Símbolo de la moneda
   - Precio formateado con separadores de miles
   - Símbolo de dólar
   - 2 decimales para valores >$1
   - 4 decimales para valores <$1

> ℹ️ Todos los precios se obtienen en tiempo real desde CoinGecko API

# 🔍 Solución de Problemas

- **Error 409**: Asegúrate de tener solo una instancia del bot ejecutándose.
- **Token inválido**: Verifica que el archivo `.env` contenga exactamente:

  ```ini
  TELEGRAM_BOT_KEY="tu_token"

- **Sin respuesta: Verifica tu conexión a internet y revisa los logs en logs/.

## 🤝 Contribuciones
1. Haz fork del proyecto
2. Crea tu rama (`git checkout -b feature/nueva-funcion`)
3. Haz commit de tus cambios (`git commit -m 'Agrega función increíble'`)
4. Push a la rama (`git push origin feature/nueva-funcion`)
5. Abre un Pull Request

## 📄 Licencia

MIT © [Misa_Vnz](https://github.com/MisaVnz)
