frutas = ['Maça','Pera','Maracujá','Morango','Manga','Melancia','Goiaba']
while True:
    for n, fruta in enumerate(frutas):
        print(f"indice{n}: {fruta}")
    print("1-Excluir fruta")
    print("2-Encerrar programa")
    opcao=input("opcao desejada: ").strip()

    match opcao:
        case "1":
            indice=int(input("informe seu indice a ser excluido: "))
            del(frutas[indice])
            print("fruta excluida com sucesso!")
            continue
        case "2":
            break
        case _:
            print("opção inválida.")
            continue