from dotenv import load_dotenv
import os
import requests
import json
from src.data.driveBot import driveBot
from src.data.transform_dataframe import transform_dataframe
from src.visualization.visualize import barv_npsmean_by, his_nps 


load_dotenv()


class TelegramBot:
    def __init__(self):
        TOKEN = os.getenv("API_KEI")
        self.url = f"https://api.telegram.org/bot{TOKEN}/"
        self.driverBot = driveBot()

    def start(self):
        update_id = None
        while True:
            update = self.get_message(update_id)
            messages = update['result']
            if messages:
                for message in messages:
                    try:
                        update_id = message['update_id']
                        chat_id = message['message']['from']['id']
                        message_text = message['message']['text']
                        answer_bot, figure_boolean = self.create_answer(message_text)
                        self.send_answer(chat_id, answer_bot, figure_boolean)

                    except:
                        pass
    
    def get_message(self, update_id):
        link_request = f"{self.url}getUpdates?timeout=1000"
        if update_id:
            link_request = f"{self.url}getUpdates?timeout=1000&offset={update_id + 1}"

        result = requests.get(link_request)
        return json.loads(result.content)

    def create_answer(self, message_text):
        dataframe = transform_data(self.driverBot.get_data())
        if message_text in ["/start", "ola", "eae", "menu", "oi", "oie"]:
            return '''Olá, eu sou o seu assistente de chat, como posso ajudar?
                    1 - NPS inteno mensal médio por setor\n
                    2 - NPS inteno mensal médio por contratação\n
                    3 - Distribuição de NPS interno\n''',0
        elif message_text == "1":
            return barv_npsmean_by(dataframe, "setor"),1
        elif message_text == "2":
            return barv_npsmean_by(dataframe, "Tipo de Contratacao"),1
        elif message_text == "3":
            return his_nps(dataframe),1
        else:
            return '''Desculpe, não entendi o que você quis dizer
                    Selecione uma das opções do menu\n
                    1 - NPS inteno mensal médio por setor\n
                    2 - NPS inteno mensal médio por contratação\n
                    3 - Distribuição de NPS interno\n''',0

    def send_answer(self, chat_id, answer, figure_boolean):
        if figure_boolean == 0:
            link_to_send = f"{self.url}sendMessage?chat_id={chat_id}&text={answer}"
            requests.get(link_to_send)
            return
        else:
            figure = r"D:\\Projetos_Git\\analise-dados-telegram-bot\\graph_last_generate.png"
            files = {open(figure, 'rb')}
            link_to_send = f"{self.url}sendPhoto?chat_id={chat_id}"
            requests.post(link_to_send, files=files)
            return
        
        