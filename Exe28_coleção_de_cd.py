import math
coleção = int(input("Quantas coleções de CD voce tem? "))
perguntas = 0
soma = 0
while perguntas < coleção:
    gasto = float(input("Quanto voce gastou nessa coleção?  "))
    soma += gasto
    perguntas += 1
media = soma / coleção
print(f"Voce tem {coleção} coleções de CD's e gastou em média R${round(media,2)}")