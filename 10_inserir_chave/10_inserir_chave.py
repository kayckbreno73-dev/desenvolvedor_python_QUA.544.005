usuario={
 'nome': "um caba ai",
     'idade': 19,
     'email':"caba@gmail.com"  
}
nova_chave=input("informe uma nova chave: ".strip().lower())
usuario[nova_chave] = input("informe o valor da nova chave: ".strip())
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")