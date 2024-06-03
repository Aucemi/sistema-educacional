from cursoSvc import CursoSvc
from agendaSvc import AgendaSvc


def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar cursos")
    print("2. Listar Cursos")
    print("3. Atualizar Cursos")
    print("4. Remover Cursos")
    print("5. Adicionar Evento/Aula")
    print("6. Listar Agenda")
    print("7. Atualizar Evento/Aula")
    print("8. Remover Evento/Aula")
    print("9. Sair")

def main():
    curso = CursoSvc()
    agendaSvc = AgendaSvc()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Titulo: ")
            descricao  = input("Descrição: ")
            carga_horaria = input("Carga Horaria: ")

            curso.adicionar_curso(titulo, descricao, carga_horaria)
            print(f"Curso {titulo} adicionado com sucesso.")


        elif opcao == '2':
            cursos = curso.listar_cursos()
            if cursos:
                for i, c in enumerate(cursos):
                    print(f"{i}. {c}")
            else:
                print("Nenhum curso cadastrado")

        elif opcao == '3':
            indice = int(input("Indice do curso a ser atualizado: "))
            titulo = input("Titulo: ")
            descricao = input("Descrição: ")
            carga_horaria = input("Carga Horaria: ")

            curso.atualizar_curso(indice, titulo, descricao, carga_horaria)
            print(f"Curso {titulo} atualizado com sucesso.")

        elif opcao == '4':
            indice = int(input("Indice do curso a ser removido: "))

            curso.remover_curso(indice)
            print("Curso removido com sucesso.")

        elif opcao == '5':
            data = input("Data: ")
            descricao = input("Descrição: ")
            tipo = input("Tipo: ")

            agendaSvc.adicionar_agenda(data, descricao, tipo)
            print("Agenda adicionado com sucesso.")

        elif opcao == '6':
            agenda_lista = agendaSvc.listar_agenda()
            if agenda_lista:
                for i, c in enumerate(agenda_lista):
                    print(f"{i}. {c}")
            else:
                print("Nenhuma agenda cadastrada")

        elif opcao == '7':
            indice = int(input("Indice da agenda a ser atualizada: "))
            data = input("Data: ")
            descricao = input("Descrição: ")
            tipo = input("Tipo: ")

            agendaSvc.atualizar_agenda(indice, data, descricao, tipo)
            print("Agenda atualizada com sucesso.")

        elif opcao == '8':
            indice = int(input("Indice da agenda a ser removida: "))

            agendaSvc.remover_agenda(indice)
            print("Agenda removida com sucesso.")

        elif opcao == '9':
            print("Saindo do programa...")
            break

        else:
            print("Escolha uma opção válida")






if __name__ == "__main__":
    main()

