x = float(input("informe um numero:").replace(",","."))
y = float(input("informe outro numero:").replace(",","."))
print(f"{'-'*20} Escolha uma operação {'-'*20}")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operador = input("operação desejada: ").strip()
match operador:
    case "1":
        print(f"resultado da soma: {x+y}")
    case "2":
        print(f"resultado da subtração: {x-y}")
    case "3":
        print(f"resultado da multiplicação: {x*y}")
    case "4":
        print(f"resultado da divisão: {x/y}")
    case _:
        print("Operação Inválida")