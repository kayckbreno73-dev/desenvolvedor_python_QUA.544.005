dias_da_semana=(
    "Domingo",
    "Segunda",
    "Terça",
    "Quarta",
    "Quinta",
    "Sexta",
    "Sábado",
)

for dia in dias_da_semana:
    print(dia)
try:
    dias_da_semana.sort()
    for dia in dias_da_semana:
        print(dias_da_semana)
except Exception as e:
    print(f"Não foi possivel ordenar. {e}")
finally:
    print("Programa Encerrado...")