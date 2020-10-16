numero = int(input("Digite um número: "))
count1 = 0
count = 1
while count1 < numero:
    fatorial = numero * (numero - count)
    count -= 1
    count1 += 1
print(fatorial)
