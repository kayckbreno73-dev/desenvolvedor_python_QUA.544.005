usuarios=[
    {
        'nome': "zeca urubu",
        'idade':"69",
        'email':"ZecaDo69@gmail.com"
    },
    {
        'nome':"urubu do pix",
        'idade':"67",
        'email':"urubudopix@gmail.com"
    },
    {
        'nome':"piru desgovernado",
        'idade':"24",
        'email':"pirusemfreio@gmail.com"
    }
]

for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")