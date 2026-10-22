import os

os.system("cls" if os.name == "nt" else "clear")

while True:

    print("1-gravar novo arquivo.")
    print("2-abrir e ler arquivo.")
    print("3-sair do programa.")

    opcao=input("opção desejada: ").strip()

    os.system("cls" if os.name == "nt" else "clear")

    match opcao:
        case "1":
            novo_texto= input("digite aqui o seu texto: ")

            novo_arquivo=input("informe um novo arquivo: ").strip()

            with open (f"15_gravando_arquivo/{novo_arquivo}.txt","w",encoding="utf-8") as f:
                f.write(novo_texto)
                continue
        case "2":
            abrir_arquivo =input("informe o nome do .txt que deseja abrir: ").strip()

            with open(f"15_gravando_arquivo/{abrir_arquivo}.txt","r", encoding="utf-8") as f:
                texto = f.read()
            print(texto)
            continue
        case "3":
            break
        case _:
            print("!!!!ERROR!!!!!")
            continue

