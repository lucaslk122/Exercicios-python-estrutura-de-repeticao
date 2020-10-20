nome = input("Nome do participante: ")
nota = []
for i in range(1,8):
    x = float(input(f"{i}º nota: "))
    nota.append(x)
print(f"Candidato: {nome}")
print(f"Melhor nota: {max(nota)}")
print(f"Pior nota: {min(nota)}")
nota.remove(min(nota))
nota.remove(max(nota))
media = sum(nota) / len(nota)
print(f"Média das notas: {round(media,2)}")
    
    