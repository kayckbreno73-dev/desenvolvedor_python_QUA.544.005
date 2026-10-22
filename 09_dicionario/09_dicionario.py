usuario={'nome': "Alex Machado",
     'idade': 41,
     'altura':1.72,
     'email':"alex@gmail.com",
     'cpf': "123.456.789.12",
     'telefone': "(61) 98765-4231"
}

print(f"nome: {usuario['nome']}")
print(f"email: {usuario.get['email']}")
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")
