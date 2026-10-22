
usuario ={  'nome': "Tomas Turbando",  'idade': 40, 'email': "tomasturbano@gmail.com", 'telefone':"(61)99999-0000",'endereço':"sao paulo" }
for chave, valor in usuario.items():
    print(f"{chave}:{valor}")
chave_escolhida = input("informe a chave a ser excluida: ").strip().lower()

del usuario[chave_escolhida]

for chave, valor in usuario.items():
    print(f"{chave} : {valor}")
  
   
   
    
                               
