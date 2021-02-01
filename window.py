import tkinter as tk

from emisor import Emisor
from order import Order



class Window:

    def __init__(self, title):
        self.win = tk.Tk()
        self.win.geometry("1300x1000")
        self.win.title(title)
        self.frameCount = 0

    def createPendingOrderDisplay(self, order, row, column):
        frame = tk.Frame(self.win, bd=3, relief="solid")

        tk.Label(frame, text=order.show_emisor_data()).grid(row=0, column=0, columnspan=3)  # Encabezado
        tk.Label(frame, text=order.show_items_as_str()).grid(row=1, column=0, columnspan=3)  # texto con pedido

        tk.Label(frame, text="Monto: ").grid(row=2, column=0)
        tk.Entry(frame).grid(row=2, column=1)
        tk.Button(frame, text="Enviar", cursor="man").grid(row=2, column=2)
        tk.Button(frame, text="Preparado").grid(row=3, column=2, padx=(2,2), pady=(1,2))


        frame.grid(row=row, column=column, padx=(10, 10), pady=(10,10))
        self.frameCount = self.frameCount + 1

        return frame

    def get_frameCount(self):
        return self.frameCount

    def createPreparedOrderDisplay(self, order, row, column):

        #tiene un boton de cerrar orden que lo manda al excel y lo borra
        #es un frame igual al pending pero sin los widgets, solo un boton de cerrar

        frame = tk.Frame(self.win, bd=3, relief="solid")

        tk.Label(frame, text=order.show_emisor_data()).grid(row=0, column=0, columnspan=3)  # Encabezado
        tk.Label(frame, text=order.show_items_as_str()).grid(row=1, column=0, columnspan=3)  # texto con pedido

        tk.Button(frame, text="Cerrar Compra").grid(row=2, column=1)
        frame.grid(row=row, column=column, padx=(10, 10), pady=(10, 10))

    def deleteDisplayOrder(self, frame):
        #se usa para borrar el frame de la pending
        frame.grid_forget()
        self.frameCount = self.frameCount - 1


    def mainloop(self):
        self.win.mainloop()

"""
root = Window("test")


order = Order(Emisor("Carlos", 192))
order.addItem("droga", 5)
order.addItem("paco", 1)

order2 = Order(Emisor("Juan", 100))
order2.addItem("pera", 3)
order2.addItem("manzana", 5)

order3 = Order(Emisor("Camila", 145))
order3.addItem("Club Social", 50)
order3.addItem("Mogul Extreme", 45)


root.createPendingOrderDisplay(order, 0, 0)
root.createPreparedOrderDisplay(order2, 1, 0)


root.createPendingOrderDisplay(order3, 0, 2)


root.mainloop()
"""

