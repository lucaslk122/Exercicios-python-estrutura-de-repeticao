n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o primeiro numero: "))
lista = []
for i in range(n1 + 1,n2):
    lista.append(i)
x = sum(lista)
print(x)