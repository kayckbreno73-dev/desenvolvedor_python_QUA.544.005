#TODO:parte 03 atividade 01
'''
Crie um programa que calcule o peso de uma pessoa em um planeta do sistema solar escolhido por ela.
NOTE:pesquisar pela aceleração da gravidade em cada planeta.
NOTE:inclua a lua na lista de planetas.

'''
gravidade = {
    "mercurio": 3.70,
    "venus": 8.87,
    "terra": 9.81,
    "lua": 1.62,
    "marte": 3.71,
    "jupiter": 24.79,
    "saturno": 10.44,
    "urano": 8.69,
    "netuno": 11.00
}

peso_terra = float(input("Digite seu peso na Terra (kg): "))

print("\nEscolha um planeta ou a Lua:")
list(map(print, gravidade.keys()))

escolha = input("\nDigite sua escolha: ").strip().lower()

if escolha in gravidade:
    calcular_peso = lambda peso, g: peso * g / gravidade["terra"]
    peso_final = calcular_peso(peso_terra, gravidade[escolha])

    print(f"\nSeu peso em {escolha.capitalize()} seria "
          f"{peso_final:.2f} kg.")
else:
    print("Opção inválida! Escolha um astro da lista.")