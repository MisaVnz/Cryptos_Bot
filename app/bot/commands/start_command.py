from telegram import Update
from telegram.ext import ContextTypes

from app_logger import get_logger

logger = get_logger("[Cryptos Bot: Command Module]")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = """
    ¡Hola! Soy *Cryptos*, un bot creado por *Misa* como proyecto para la materia Transmisión de Datos.

    Puedo proporcionarte datos en tiempo real del precio de
    criptomonedas, pero porfa uno a la vez, toy chiquito :(.
    Estas son las monedas disponibles:

    • Bitcoin: /BTC
    • Ethereum: /ETH
    • Solana: /SOL
    • Binance Coin: /BNB
    • Tron: /TRX

    ¡Usa alguno de estos comandos para obtener el precio actual!
    """
    # Enviar el mensaje de bienvenida al usuario
    await update.message.reply_text(welcome_text, parse_mode='Markdown')
    logger.info("Enviado mensaje de bienvenida al usuario")