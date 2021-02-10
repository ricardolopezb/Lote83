import tkinter as tk

from chatbot import Chatbot

from functools import partial


class Window:
    bot = Chatbot()

    def __init__(self, title):
        self.win = tk.Tk()
        self.win.geometry("1300x1000")
        self.win.title(title)
        self.frameCount = 0

    def enviarCommandFunction(self, order, entry):
        self.bot.sendMonto(order.emisor.get_id(), entry.get())



    def createPendingOrderDisplay(self, order, row, column, func):
        frame = tk.Frame(self.win, bd=3, relief="solid")

        tk.Label(frame, text=order.show_emisor_data()).grid(row=0, column=0, columnspan=3)  # Encabezado
        tk.Label(frame, text=order.show_items_as_str()).grid(row=1, column=0, columnspan=3)  # texto con pedido

        tk.Label(frame, text="Monto: ").grid(row=2, column=0)
        entry = tk.Entry(frame)
        entry.grid(row=2, column=1)

        emisorId = order.emisor.get_id()

        tk.Button(frame, text="Problema", command=partial(self.launchSupportWindow, emisorId)).grid(row=3, column=1)
        tk.Button(frame, text="Enviar", command=partial(self.enviarCommandFunction, order, entry)).grid(row=2, column=2)
        tk.Button(frame, text="Preparado", command=partial(func, order, frame)).grid(row=3, column=2, padx=(2,2), pady=(1,2))


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
        self.frameCount = self.frameCount + 1

    def deleteDisplayOrder(self, frame):
        #se usa para borrar el frame de la pending
        frame.grid_forget()
        self.frameCount = self.frameCount - 1


    def mainloop(self):
        self.win.mainloop()

    def launchSupportWindow(self, chatId):
        suppWin = tk.Tk()
        suppWin.geometry("695x415")
        suppWin.title('Mensaje de Error')

        textBox = tk.Text(suppWin)
        textBox.pack(side=tk.LEFT)


        sendButton = tk.Button(suppWin, text="Enviar", height="400" ,command=partial(self.supportButton, chatId, textBox))
        sendButton.pack(side=tk.RIGHT)

        suppWin.mainloop()

    def supportButton(self, chatId, textbox):
        message = self.getText(textbox)
        self.bot.send_message(chatId, message)


    def getText(self, textBox):
        return textBox.get("1.0", "end-1c")



