from dotenv import load_dotenv
import gspread
import json
import os

load_dotenv()

class driveBot:
    def __init__(self):
        self.gc = gspread.service_account(filename = "credentials.json")

    def get_data(self):
        sh = self.gc.open_by_key("1ct7p9CuQpuQK3860SiQup0vD6yyZEioKcKgyGM3bWhI")
        worksheet = sh.sheet1
        return worksheet.get_all_values()