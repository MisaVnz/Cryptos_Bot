import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.TELEGRAM_BOT_KEY: str = os.getenv("TELEGRAM_BOT_KEY")
        self.LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
        self.API_URL: str = os.getenv("API_URL", "https://api.coingecko.com/api/v3/simple/price")
        self.CURRENCIES: list = os.getenv("CURRENCIES", "bitcoin,ethereum,solana,binancecoin,trondao").split(",")
        self.APP_NAME: str = os.getenv("APP_NAME", "Cryptos Bot")
        self.AUTHOR_NAME: str = os.getenv("AUTHOR_NAME", "Misa")

    @classmethod
    def get_telegram_bot_key(self) -> str:
        """Devuelve la key del bot de Telegram."""
        return self.TELEGRAM_BOT_KEY
    
    @classmethod
    def get_app_name(self) -> str:
        """Devuelve el nombre de la aplicación."""
        return self.APP_NAME
    
    @classmethod
    def get_author_name(self) -> str:
        """Devuelve el nombre del autor de la aplicación."""
        return self.AUTHOR_NAME