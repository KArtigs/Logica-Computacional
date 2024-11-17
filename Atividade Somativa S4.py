# ATIVIDADE SOMATIVA SEMANA 4
# KELLY CRISTINE ARTIGAS PINTO
# TECNOLOGIA EM ANALISE E DESENVOLVIMENTO DE SISTEMAS
# LOGICA COMPUTACIONAL - PYTHON
# 10/11/2024

estudantes = []  # Lista para armazenar os nomes dos estudantes

while True:
    # Exibe o menu principal (variavel opmp)
    print("Menu Principal:")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("6. Sair")

    # Recebe a opção do usuário para o menu principal
    menu_principal = input("Selecione a opção desejada: ")

    if menu_principal == "1":
        opmp = "Estudantes"
    elif menu_principal == "2":
        opmp = "Disciplinas"
        print(f"{opmp} EM DESENVOLVIMENTO")
        continue
    elif menu_principal == "3":
        opmp = "Professores"
        print(f"{opmp} EM DESENVOLVIMENTO")
        continue
    elif menu_principal == "4":
        opmp = "Turmas"
        print(f"{opmp} EM DESENVOLVIMENTO")
        continue
    elif menu_principal == "5":
        opmp = "Matrículas"
        print(f"{opmp} EM DESENVOLVIMENTO")
        continue
    elif menu_principal == "6":
        print("Você escolheu Sair! Encerrando o programa.")
        break
    else:
        print("Opção inválida")
        continue

    # Exibe a opção desejada do menu principal em seguida o menu operacional (variavel opmo)
    print(f"Bem vindo ao portal {opmp}!")
    print("Menu Operacional:")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar ao menu anterior")

    # Recebe a opção do usuário para o menu operacional
    menu_operacional = input("Selecione a opção desejada: ")

    if opmp == "Estudantes":
        if menu_operacional == "1":
            nome_estudante = input("Digite o nome do estudante: ")
            estudantes.append(nome_estudante)
            print(f"Estudante {nome_estudante} incluído com sucesso!")
        elif menu_operacional == "2":
            if not estudantes:
                print("Não há estudantes cadastrados.")
            else:
                print("Lista de Estudantes:")
                for estudante in estudantes:
                    print(estudante)
        elif menu_operacional == "3":
            opmo = "Atualizar"
            print(f"{opmo} EM DESENVOLVIMENTO")
        elif menu_operacional == "4":
            opmo = "Excluir"
            print(f"{opmo} EM DESENVOLVIMENTO")
        elif menu_operacional == "5":
            print("Voltando ao menu anterior")
            continue
        else:
            print("Opção inválida")
            continue
    else:
        opmo = menu_operacional
        print(f"Você escolheu {opmo}")
