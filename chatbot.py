from telegram.ext import Updater, CommandHandler
import requests
import json

class Chatbot:
    def __init__(self):
        self.baseLink = "https://api.telegram.org/bot1693058268:AAHvPADd2P8H9_1qriiRqFsEjiBw51ReCBQ"


#para seleccionar el ultimo mensaje del update, buscar el index -1

    def get_updates(self, offset=None):
        url = self.baseLink + "/getUpdates?timeout=100"
        if offset:
            url = url + "&offset=" + str(offset+1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_pedidoRecibido(self, chatId):
        reply = "Hemos recibido tu pedido. Si hay algun problema o nos falta algun producto, nos comunicaremos"
        url = self.baseLink + ("/sendMessage?chat_id={}&text={}".format(chatId, reply))
        requests.get(url)

    def send_total(self, chatId, monto):
        total = "$" + str(monto)
        url = self.baseLink + ("/sendMessage?chat_id={}&text={}".format(chatId, total))
        requests.get(url)
    def send_prepared(self, chatId):
        reply = "Tu pedido ya esta preparado, podes retirarlo cuando quieras."
        url = self.baseLink + ("/sendMessage?chat_id={}&text={}".format(chatId, reply))
        requests.get(url)
    def send_message(self, chatId, message):
        url = self.baseLink + ("/sendMessage?chat_id={}&text={}".format(chatId, message))
        requests.get(url)

    def delete_message(self, chatId, messageId):
        url = self.baseLink + ("/deleteMessage?chat_id={}&message_id={}").format(chatId, messageId)
        requests.get(url)

    def sendMonto(self, chatId, monto):
        reply = "El monto de su compra es de $" + monto
        url = self.baseLink + ("/sendMessage?chat_id={}&text={}".format(chatId, reply))
        requests.get(url)


