import os
os.system("cls" if os.name == "nt" else "clear")

while True:
    aluno=input("informe o nome do aluno: ").strip().title()
    try:
        nota=float(input("informe a nota de 0-10: ").replace(',','.'))
        if nota >=0 and nota <= 10:
            if nota>=7:
                print(f"{aluno} está aprovado")
            elif nota >=5:
                print(f"{aluno} está de recuperação")
            else:
                print(f"{aluno} está reprovado")
        else:
            print("nota inválida")
    except Exception as e:
        print(f"não foi possivel calcular a media {e}.")
    continuar=input("deseja continuar? 'sim' para prosseguir. Qualquer outro valor pra encerrar:".strip().lower())