try:
    nome =input("informe seu nome: ").strip().title()
    idade=int(input("informe sua idade: "))
    
    print(f"o Nome de usuário é {nome}")
    print(f"a Idade do Usuário é {idade} anos ")
except Exception as e:
    print("não foi possivel executar a ação!")
    print(e)
finally:
    print("programa finalizado com sucesso")
   
    