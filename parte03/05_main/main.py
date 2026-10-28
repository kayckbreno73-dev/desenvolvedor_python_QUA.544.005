import math
import os

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def raiz(n):
    return math.sqrt(n)

def main():
    limpar()
    n = int(input("informe um número inteiro: "))
    print(f"a raiz de {n} é {raiz(n)}.")


if __name__ == "__main__":
    main()
    