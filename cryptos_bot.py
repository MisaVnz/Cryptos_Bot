from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from app.core.price_bitcoin import obtener_precio_bitcoin
from app.core.price_ethereum import obtener_precio_ethereum
from app.core.price_solana import obtener_precio_solana
from app.core.price_bnb import obtener_precio_bnb
from app.core.price_tron import obtener_precio_tron
from dotenv import load_dotenv
import os
import logging

load_dotenv()

# Obtiene el token de forma segura desde las variables de entorno
TOKEN = os.getenv("TELEGRAM_BOT_KEY")  

# Configura logging para ver errores
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def format_price(price, symbol):
    return f"💰 {symbol}: ${price:,.2f}" if price else "❌ Error al obtener precio"

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
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        precio = obtener_precio_bitcoin()
        await update.message.reply_text(format_price(precio, "BTC"))
    except Exception as e:
        logger.error(f"Error en /BTC: {e}")
        await update.message.reply_text("❌ Error al obtener el precio de Bitcoin")

async def eth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        precio = obtener_precio_ethereum()
        await update.message.reply_text(format_price(precio, "ETH"))
    except Exception as e:
        logger.error(f"Error en /ETH: {e}")

async def sol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        precio = obtener_precio_solana()
        await update.message.reply_text(format_price(precio, "SOL"))
    except Exception as e:
        logger.error(f"Error en /SOL: {e}")

async def bnb(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        precio = obtener_precio_bnb()
        await update.message.reply_text(format_price(precio, "BNB"))
    except Exception as e:
        logger.error(f"Error en /BNB: {e}")

async def trx(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        precio = obtener_precio_tron()
        await update.message.reply_text(format_price(precio, "TRX"))
    except Exception as e:
        logger.error(f"Error en /TRX: {e}")

async def post_init(application: Application):
    await application.bot.delete_webhook(drop_pending_updates=True)

def main():
    # Verifica que el token esté disponible
    if not TOKEN:
        logger.error("❌ No se encontró TELEGRAM_BOT_KEY en las variables de entorno")
        raise ValueError("Token de Telegram no configurado")

    application = Application.builder().token(TOKEN).post_init(post_init).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("BTC", btc))
    application.add_handler(CommandHandler("ETH", eth))
    application.add_handler(CommandHandler("SOL", sol))
    application.add_handler(CommandHandler("BNB", bnb))
    application.add_handler(CommandHandler("TRX", trx))

    logger.info("Bot iniciado. Usa /start para ver las opciones")
    application.run_polling()

if __name__ == "__main__":
    main()