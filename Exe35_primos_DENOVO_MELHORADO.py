numero = int(input("Digite um número: "))
lista = []
for i in range(numero + 1):
    if i % 2 == 1 and i != 2:
        lista.append(i)
print(f"Números primos: {lista} ")