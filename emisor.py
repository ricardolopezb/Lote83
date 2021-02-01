class Emisor:

    def __init__(self, nombre, lote, id):
        self.nombre = nombre
        self.lote = str(lote)
        self.id = id

    def get_nombre(self):
        return self.nombre
    def get_lote(self):
        return self.lote
    def get_id(self):
        return self.id

