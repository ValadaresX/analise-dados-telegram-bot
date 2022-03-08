from msilib.schema import Class
from urllib import request
from dotenv import load_dotenv
import os
import requests

load_dotenv()


class TelegramBot:
    def __init__(self):
        TOKEN = os.getenv("API_KEY")
        self.url = f"https://api.telegram.org/bot{TOKEN}/"
    
    def get_message(self):
        link_request = f"{self.url}getUpdate?timeout=1000"
        result = request.get(link_request)
        return result