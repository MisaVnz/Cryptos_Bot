import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.TELEGRAM_BOT_KEY = os.getenv("TELEGRAM_BOT_KEY")
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
        self.API_URL = os.getenv("API_URL", "https://api.coingecko.com/api/v3/simple/price")
        self.CURRENCIES = os.getenv("CURRENCIES", "bitcoin,ethereum,solana,binancecoin,trondao").split(",")
        self.APP_NAME = os.getenv("APP_NAME", "Cryptos Bot")
        self.AUTHOR_NAME = os.getenv("AUTHOR_NAME", "Misa")