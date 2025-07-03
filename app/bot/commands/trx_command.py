from telegram import Update
from telegram.ext import ContextTypes

from core import obtener_precio_tron
from app_logger import get_logger
from bot.utils import format_price

logger = get_logger("[Cryptos Bot: Command Module]")

async def trx(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        precio = obtener_precio_tron()
        await update.message.reply_text(format_price(precio, "TRX"))
    except Exception as e:
        logger.error(f"Error en /TRX: {e}")