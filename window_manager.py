from window import Window
from chatbot import Chatbot
from order_maker import OrderMaker
import threading
import time
import winsound

class WindowManager:

    bot = Chatbot()
    orderMaker = OrderMaker()

    def __init__(self):
        self.pendientes = Window("Ordenes Pendientes")
        self.preparadas = Window("Ordenes Preparadas")
        self.update_id = None

    def startServer(self):
        print('...')
        updates = self.bot.get_updates(offset=self.update_id)
        updates = updates['result']
        if updates:
            for item in updates:
                self.update_id = item['update_id']
                try:
                    message = item["message"]["text"]
                    # armar ordenes y updatear la window
                except:
                    message = None

                sender = item["message"]["from"]["id"]

                if message == '/start':
                    self.bot.send_message(sender,
                                     "Bienvenido al Lote Islas 83!\nPara hacer un pedido, escribir un mensaje con el siguiente formato\n\n[Nombre] [Num. de Lote]\n[Cantidad] [Producto]\n[Cantidad] [Producto]\n[Cantidad] [Producto]")
                    self.bot.delete_message(sender, item["message"]["message_id"])

                if len(message) > 6:
                    orden = self.orderMaker.generateOrder(message, sender)
                    self.add_ordenPendiente(orden)

                    # hacer el display de la orden

                    self.bot.send_pedidoRecibido(sender)
        time.sleep(1)
        self.startServer()

    def startWindows(self):
        threading.Thread(target=self.startServer).start()
        self.pendientes.mainloop()
        self.preparadas.mainloop()


    def moveFrame(self, order, frame):
        self.pendientes.deleteDisplayOrder(frame)
        where = self.findSlot(self.preparadas)
        self.preparadas.createPreparedOrderDisplay(order, where[0], where[1])
        self.bot.send_prepared(order.emisor.get_id())



    def add_ordenPendiente(self, order):
        where = self.findSlot(self.pendientes)
        func = self.moveFrame
        self.pendientes.createPendingOrderDisplay(order, where[0], where[1], func)
        self.pendientes.win.update()
        winsound.Beep(440, 1000)

    def findSlot(self, window):
        framesInDest = window.get_frameCount()
        row = 0

        if framesInDest >= 16:
            row = row + 4
        elif framesInDest >= 12:
            row = row + 3
        elif framesInDest >= 8:
            row = row + 2
        elif framesInDest >= 4:
            row = row + 1

        i = framesInDest
        while i > 4:
            i = i - 4

        return [row, i]
