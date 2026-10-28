import os 

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def boas_vindas(nome):
    return f"{nome}, seja bem vindo!"

limpar()
nome=input("informe seu nome: ").strip().title()
print(boas_vindas(nome))