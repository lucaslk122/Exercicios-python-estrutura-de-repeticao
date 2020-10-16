from statistics import mean
qtd = int(input("Serão quantas notas? "))
perguntas = 0
lista = []
while perguntas < qtd:
    num = float(input("Digite a nota: "))
    perguntas += 1
    lista.append(num)
media = mean(lista)
print(f"A média arimética das notas digitadas  é {round(media,2)}")
