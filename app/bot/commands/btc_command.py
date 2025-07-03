from telegram import Update
from telegram.ext import ContextTypes

from app.core import obtener_precio_bitcoin
from app.app_logger import get_logger
from app.bot.utils import format_price

logger = get_logger("[Cryptos Bot: Command Module]")

async def btc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        precio = obtener_precio_bitcoin()
        await update.message.reply_text(format_price(precio, "BTC"))
    except Exception as e:
        logger.error(f"Error en /BTC: {e}")
        await update.message.reply_text("❌ Error al obtener el precio de Bitcoin")