"""
Clase Order

Maneja una lista de tuples con la informacion del item y la cantidad

"""


class Order:
    def __init__(self, emisor):
        self.monto = None
        self.orderList = []
        self.emisor = emisor


    def addItem(self, itemStr, quantity):
        self.orderList.append((itemStr, quantity))

    def show_items_as_str(self):
        """:returns String"""
        toDisplay = ''
        for (item, quantity) in self.orderList:
            toDisplay = toDisplay + '- ' +str(quantity) + '\t' + item + "\n"
        return toDisplay

    def show_emisor_data(self):
        return 'Cliente: ' + self.emisor.get_nombre() + ' - Lote: ' + self.emisor.get_lote()

    def archivar_orden(self):
        #guardar la orden en un excel
        pass
