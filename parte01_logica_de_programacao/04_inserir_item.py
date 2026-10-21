import os
tarefas =[]
os.system("cls" if os.name == "nt" else "clear")
while True:
    print("1 - inserir nova tarefa na lista")
    print("2 - finalizar e exibir tarefa na lista")
    opcao = input("opção desejada: ".strip())
    match opcao:
        case "1":
            nova_tarefa=input("informe uma nova tarefa:")
            tarefas.append(nova_tarefa)
            continue
        case "2":
            os.system("cls" if os.name == "nt" else "clear")

            for n, tarefa in enumerate(tarefas, start=1):
                print(f"{n}ª tarefa: {tarefa}")
            break