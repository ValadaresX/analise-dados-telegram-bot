from msilib.schema import Class
from dotenv import load_dotenv
import os

load_dotenv()


class TelegramBot:
    def __init__(self):
        TOKEN = os.getenv("API_KEY")
        self.url = f"https://api.telegram.org/bot{TOKEN}/"