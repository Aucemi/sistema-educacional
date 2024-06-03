from curso import Curso


class CursoSvc:
    def __init__(self):
        self.cursos = []

    def adicionar_curso(self, titulo, descricao, carga_horaria):
        novo_curso = Curso(titulo, descricao, carga_horaria)
        self.cursos.append(novo_curso)

    def listar_cursos(self):
        return self.cursos

    def atualizar_curso(self, indice, titulo, descricao, carga_horaria):
        self.cursos[indice] = Curso(titulo, descricao, carga_horaria)

    def remover_curso(self, indice):
        self.cursos.pop(indice)

