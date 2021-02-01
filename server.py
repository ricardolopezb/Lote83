from chatbot import Chatbot
from order_maker import OrderMaker
from window import Window
from window_manager import WindowManager
import threading
import time


def startServer():
    update_id = None
    while True:
        print('...')
        updates = bot.get_updates(offset=update_id)
        updates = updates['result']
        if updates:
            for item in updates:
                update_id = item['update_id']
                try:
                    message = item["message"]["text"]
                    # armar ordenes y updatear la window
                except:
                    message = None

                sender = item["message"]["from"]["id"]

                if message == '/start':
                    bot.send_message(sender, "Bienvenido al Lote Islas 83!\nPara hacer un pedido, escribir un mensaje con el siguiente formato\n\n[Nombre] [Num. de Lote]\n[Cantidad] [Producto]\n[Cantidad] [Producto]\n[Cantidad] [Producto]")
                    bot.delete_message(sender, item["message"]["message_id"])

                if len(message) > 6:
                    orden = orderMaker.generateOrder(message, sender)
                    window.add_ordenPendiente(orden)

                    # hacer el display de la orden

                    bot.send_pedidoRecibido(sender)
        time.sleep(1)

bot = Chatbot()
orderMaker = OrderMaker()
window = WindowManager()


threadWindows = threading.Thread(target=window.startWindows(), args=())
threadServer = threading.Thread(target=startServer(), args=())


#threadWindows.start()
threadServer.start()


