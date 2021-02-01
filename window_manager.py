from window import Window
from chatbot import Chatbot

class WindowManager:

    bot = Chatbot()

    def __init__(self):
        self.pendientes = Window("Ordenes Pendientes")
        self.preparadas = Window("Ordenes Preparadas")


    def startWindows(self):
        self.pendientes.mainloop()
        self.preparadas.mainloop()


    def moveFrame(self, order):
        self.pendientes.deleteDisplayOrder(order)
        where = self.findSlot(self.preparadas)
        self.preparadas.createPreparedOrder(order, where[0], where[1])
        self.bot.send_prepared(order.emisor.get_id())



    def add_ordenPendiente(self, order):
        where = self.findSlot(self.pendientes)
        self.pendientes.createPendingOrderDisplay(order, where[0], where[1])

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

        return [row, i - 1]
