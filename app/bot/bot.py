from telegram.ext import Application, CommandHandler

from app.settings import Config
from app.app_logger import get_logger
from app.bot.commands import start, eth, sol, bnb, trx, btc

logger = get_logger("[Cryptos Bot]")

TOKEN = Config().TELEGRAM_BOT_KEY  

async def post_init(application: Application):
    """Función que se ejecuta después de que la aplicación se haya inicializado."""
    logger.info("🔗 Configurando el webhook del bot de Telegram...")
    await application.bot.delete_webhook(drop_pending_updates=True)

def main():
    # Verifica que el token esté 
    
    logger.info("🔗 Iniciando el bot de Telegram...")

    if not TOKEN:
        logger.error("❌ No se encontró TELEGRAM_BOT_KEY en las variables de entorno")
        raise ValueError("Token de Telegram no configurado")
    else:
        logger.info("✅ Token de Telegram encontrado")

    application = Application.builder().token(TOKEN).post_init(post_init).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("BTC", btc))
    application.add_handler(CommandHandler("ETH", eth))
    application.add_handler(CommandHandler("SOL", sol))
    application.add_handler(CommandHandler("BNB", bnb))
    application.add_handler(CommandHandler("TRX", trx))
    
    try:
        application.run_polling()
        logger.info("Bot iniciado. Usa /start para ver las opciones")
    except Exception as e:
        logger.error(f"Error al iniciar el bot: {e}")
        raise e