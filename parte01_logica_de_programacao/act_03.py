import os

nomes = ["Alex", "Charllote", "Scarlet", "John", "Jason", "Michael", "Connor"]

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    limpar_tela()

    for n, nome in enumerate(nomes):
        print(f"Índice {n}: {nome}")

    print("\n1 - Alterar item da lista")
    print("2 - Finalizar")

    opcao = input("Opção desejada: ").strip()

    match opcao:
        case "1":
            try:
                indice = int(input("Informe o índice a ser alterado: "))

                if 0 <= indice < len(nomes):
                    nomes[indice] = input(
                        "Informe o novo nome: "
                    ).strip().title()

                    print("Item da lista alterado com sucesso!")
                else:
                    print("Índice inválido!")

            except ValueError:
                print("Digite um índice numérico válido!")

            input("\nPressione Enter para continuar...")

        case "2":
            limpar_tela()
            print("=== LISTA FINAL ===")

            for n, nome in enumerate(nomes):
                print(f"Índice {n}: {nome}")

            print("\nPrograma finalizado!")
            break

        case _:
            print("Opção inválida!")
            input("\nPressione Enter para continuar...")