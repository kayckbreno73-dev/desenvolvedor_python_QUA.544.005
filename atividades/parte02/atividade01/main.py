#crie um programa que faça as seguintes operações;
#cadastra um novo usuario(nome, email, telefone, cpf)
#lista todos os usuarios cadastrados
#altera os dados de um usuário
#exclui um usuario
#grava os dados de todos os usuários em um .json
#abre arquivo .json e lista todos os usuarios cadastrados nele

import json

usuarios = []

while True:
    print("\n- MENU -")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Alterar usuário")
    print("4 - Excluir usuário")
    print("5 - Salvar usuários em JSON")
    print("6 - Abrir arquivo JSON")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        cpf = input("CPF: ")

        usuario = {
            "nome": nome,
            "email": email,
            "telefone": telefone,
            "cpf": cpf
        }

        usuarios.append(usuario)
        print("Usuário cadastrado!")

    elif opcao == "2":
        for usuario in usuarios:
            print(usuario)

    elif opcao == "3":
        cpf = input("Digite o CPF do usuário que deseja alterar: ")

        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                usuario["nome"] = input("Novo nome: ")
                usuario["email"] = input("Novo email: ")
                usuario["telefone"] = input("Novo telefone: ")
                usuario["cpf"] = input("Novo CPF: ")
                print("Usuário alterado!")
                break
        else:
            print("Usuário não encontrado!")

    elif opcao == "4":
        cpf = input("Digite o CPF do usuário que deseja excluir: ")

        for usuario in usuarios:
            if usuario["cpf"] == cpf:
                usuarios.remove(usuario)
                print("Usuário excluído!")
                break
        else:
            print("Usuário não encontrado!")

    elif opcao == "5":
        with open("usuarios.json", "w", encoding="utf-8") as arquivo:
            json.dump(usuarios, arquivo, ensure_ascii=False, indent=4)

        print("Dados salvos em usuarios.json!")

    elif opcao == "6":
        try:
            with open("usuarios.json", "r", encoding="utf-8") as arquivo:
                usuarios = json.load(arquivo)

            for usuario in usuarios:
                print(usuario)

        except FileNotFoundError:
            print("Arquivo JSON não encontrado!")

    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")
