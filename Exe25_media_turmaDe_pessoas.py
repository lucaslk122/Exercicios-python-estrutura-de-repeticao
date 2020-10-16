from statistics import mean
n = int(input("Quantas pessoas tem na turma? "))
pergunta = 0
lista = []
while pergunta < n:
    idade = int(input("Digite a idade das pessoas: "))
    lista.append(idade)
    pergunta += 1
media = mean(lista)
if media < 0 or media <= 25:
    print("A turma é jovem")
elif media > 26 and media < 60:
    print("A turma é adulta")
else:
    print("A turma é idosa")