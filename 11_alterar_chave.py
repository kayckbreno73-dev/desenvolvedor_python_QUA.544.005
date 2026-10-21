import os

usuario = {
    'nome': "Tomas Turbando",
    'idade': 40,
    'email': "alex@gmail.com",
    'telefone': "(61) 96666-6666"
}

os.system("cls" if os.name == "nt" else "clear")

while True:
    for chave, valor in usuario.items():
        print(f"{chave}: {valor}")

    chave_escolhida = input(
        "Informe o nome da chave que deseja alterar ou Enter para encerrar: "
    ).strip().lower()

    if chave_escolhida:
        if chave_escolhida in usuario:
            usuario[chave_escolhida] = input(
                "Informe o novo valor: "
            ).strip()
        else:
            print("Chave não encontrada!")
        continue
    else:
        break