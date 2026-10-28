import modulo

modulo.limpar()
while True:
    print("1 - Calcular Área Do Quadrilátero")
    print("2 - Calcular área do circulo")
    print("3 - Calcular comprimento do circulo")
    print("4 - Sair do programa")
    opcao=input("opção desejada: ").strip()
    modulo.limpar()
    match opcao:
        case "1":
            b=float(input("informe a base:").replace(",","."))
            h=float(input("informe a altura:").replace(",","."))
            a=modulo.a_quad(b, h)
            print(f"Área do quadriláttero: {a}.")
            continue
        case "2":
            r = float(input("informe o valor do raio").replace(",","."))
            a = modulo.a_circulo(r)
            print(f"Área do circulo:{a}.")
            continue
        case "3":
            r = float(input("Informe o raio: ").replace(",","."))
            a = modulo.comprimento_circulo(r)
            print(f"comprimento do circulo: {a}")
            continue
        case "4":
            break
        case _:
            print("opção inválida.")
            continue