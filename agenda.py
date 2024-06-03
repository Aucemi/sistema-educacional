class Agenda:
    def __init__(self, data, descricao, tipo):
        self.data = data
        self.descricao = descricao
        self.tipo = tipo

    def __repr__(self):
        return f"Agenda(data='{self.data}', descricao='{self.descricao}', tipo='{self.tipo}')"
