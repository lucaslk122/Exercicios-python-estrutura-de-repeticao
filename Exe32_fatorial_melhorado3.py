import math
numero = int(input("Digite o numero que quer realizar a fatorial : "))
count = numero
fatorial = math.factorial(numero)

for i in range(numero - 1):
    print(count, end=" . ")
    count -= 1
print(f"1 = {fatorial}")