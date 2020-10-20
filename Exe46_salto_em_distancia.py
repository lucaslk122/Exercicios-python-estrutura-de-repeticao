salto = []
nome = input("Nome do atletra: ")
for i in range(1,6):
    x = float(input(f"{i}º salto: "))
    salto.append(x)
print(f"Melhor salto: {max(salto)}")
print(f"Pior salto: {min(salto)}")
salto.remove(min(salto))
salto.remove(max(salto))
media = sum(salto) / 3
print(f"Média dos saltos: {round(media,2)}m")
print(f"""Resultado final:
{nome} : {round(media,2)}m""")