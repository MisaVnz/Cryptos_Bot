from telegram import Update
from telegram.ext import ContextTypes

from app.core import obtener_precio_solana
from app.app_logger import get_logger
from app.bot.utils import format_price

logger = get_logger("[Cryptos Bot: Command Module]")

async def sol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        precio = obtener_precio_solana()
        await update.message.reply_text(format_price(precio, "SOL"))
    except Exception as e:
        logger.error(f"Error en /SOL: {e}")