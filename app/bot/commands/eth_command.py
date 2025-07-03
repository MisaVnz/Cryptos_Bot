from telegram import Update
from telegram.ext import ContextTypes

from core import obtener_precio_ethereum
from app_logger import get_logger
from bot.utils import format_price

logger = get_logger("[Cryptos Bot: Command Module]")

async def eth(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        precio = obtener_precio_ethereum()
        await update.message.reply_text(format_price(precio, "ETH"))
    except Exception as e:
        logger.error(f"Error en /ETH: {e}")