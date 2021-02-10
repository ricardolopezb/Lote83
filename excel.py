import pandas as pd

class Excel:
    def __init__(self):
        self.data = {"Fecha": [], "Lote": [], "Nombre": [], "Monto": []}
        self.df = pd.DataFrame(self.data)

    def addRow(self, date, lote, nombre, monto):
        self.df = self.df.append({"Fecha": date, "Lote":lote, "Nombre":nombre, "Monto":monto}, ignore_index=True)
        self.df.to_excel("lote83.xlsx", sheet_name="Ventas")
    def print(self):
        print(self.df)

"""excel = Excel()
excel.print()
excel.addRow(2021, 145, "ricardo", 1000)
excel.addRow(2001, 696, "camila", 500)

excel.df.to_excel("lote83.xlsx", sheet_name="Ventas")

excel.addRow(2991, 20, "droga", 100)

excel.df.to_excel("lote83.xlsx", sheet_name="Ventas")
print("---------")
excel.print()"""


