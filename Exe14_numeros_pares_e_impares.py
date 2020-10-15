pergunta = 0
lista = []
while pergunta < 10:
    num = int(input("Digite um numero inteiro: "))
    lista.append(num)
    pergunta +=1
pares = 0
impares = 0
for i in lista:
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1
print (f"Temos {pares} numeros pares e {impares} numeros impares")
