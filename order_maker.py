from order import Order
from emisor import Emisor


class OrderMaker:
    def generateOrder(self, message, senderID):
        divMessage = message.split('\n')
        senderSplit = divMessage[0].split(" ", 1)

        emisor = Emisor(senderSplit[0], senderSplit[1], senderID)

        itemStrings = divMessage[1:]
        orden = Order(emisor)

        for item in itemStrings:
            divItem = item.split(' ', 1)
            cant = divItem[0]
            producto = divItem[1]
            orden.addItem(producto, cant)

        return orden


