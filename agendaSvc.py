from agenda import Agenda


class AgendaSvc:
    def __init__(self):
        self.agenda = []

    def adicionar_agenda(self, data, descricao, tipo):
        novo_agenda = Agenda(data, descricao, tipo)
        self.agenda.append(novo_agenda)

    def listar_agenda(self):
        return self.agenda

    def atualizar_agenda(self, indice, data, descricao, tipo):
        self.agenda[indice] = Agenda(data, descricao, tipo)

    def remover_agenda(self, indice):
        self.agenda.pop(indice)

