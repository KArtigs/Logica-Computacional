# ATIVIDADE FORMATIVA SEMANA 3
# KELLY CRISTINE ARTIGAS PINTO
# TECNOLOGIA EM ANALISE E DESENVOLVIMENTO DE SISTEMAS
# LOGICA COMPUTACIONAL - PYTHON
# 22/10/2024

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
    elif menu_principal == "3":
        opmp = "Professores"
    elif menu_principal == "4":
        opmp = "Turmas"
    elif menu_principal == "5":
        opmp = "Matrículas"
    elif menu_principal == "6":
        print("Você escolheu Sair! Encerrando o programa.")
        break
    elif menu_principal != "1":
        print(f"Bem vindo ao portal {opmp}!")
        print("EM DESENVOLVIMENTO")
        break
    else:
        print("Opção inválida")
        continue

    #Exibe a opção desejada do menu principal em seguida o menu operacional (variavel opmo)  
    print(f"Bem vindo ao portal {opmp}!")
    print("Menu Operacional:")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Voltar ao menu anterior")

    # Recebe a opção do usuário para o menu operacional
    menu_operacional = input("Selecione a opção desejada: ")

    if menu_operacional == "1":
        opmo = "Incluir"
    elif menu_operacional == "2":
        opmo = "Listar"
    elif menu_operacional == "3":
        opmo = "Atualizar"
    elif menu_operacional == "4":
        opmo = "Excluir"
    elif menu_operacional == "5":
        print("Voltando ao menu anterior")
        continue
    else:
        print("Opção inválida")
        continue

    #Imprime a opção selecionada no menu operacional e encerra a execução 
    print(f"Você escolheu {opmo}")
   
