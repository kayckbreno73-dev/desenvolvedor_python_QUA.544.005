import os

usuarios=[]

os.system("cls" if os.name == "nt" else "clear")

while True:
    print("1-Cadastrar novo usuario")
    print("2-exibir lista de usuarios")
    print("3-sair do programa")
    opcao=input("opcao desejada: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            usuario={}
            usuario['nome']=input("informe seu nome: ".title().strip())
            usuario['idade']=int(input("informe sua idade: ".strip().lower()))
            usuario['email']=input("informe o CPF: ".strip())

            usuarios.append(usuario)
            print(f"{usuario.get('nome')} cadastrado com sucesso!")
            continue

        case "2":
            for usuario in usuarios:
                for chave, valor in usuario.items():
                    print(f"{chave.capitalize()} : {valor}")
                print(f"{'-'*40}")
            continue

        case "3":
            break

        case _:
            print("opção inválida.")
