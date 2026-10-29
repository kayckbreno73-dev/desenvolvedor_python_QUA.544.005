'''TODO:parte 03 atividade 02
Crie um programa em que o usuario informe um numero inteiro e o programa retorne a sequencia fibonacci'''

print("SEQUÊNCIA DE FIBONACCI")

n = int(input("Digite a quantidade de números da sequência: "))

a = 0
b = 1
i = 0

if n <= 0:
    print("Digite um número inteiro positivo.")
else:
    while i < n:
        print(a, end=" ")
        proximo = a + b
        a = b
        b = proximo
        i += 1