class Curso:
    def __init__(self, titulo, descricao, carga_horaria):
        self.titulo = titulo
        self.descricao = descricao
        self.carga_horaria = carga_horaria

    def __repr__(self):
        return f"Curso(titulo='{self.titulo}', descricao='{self.descricao}', carga_horaria='{self.carga_horaria}')"