import math
from math import factorial
num = int(input("Digite um numero: "))
#print(f"o fatorial de {num} é {math.factorial(num)}")
factorial = 1
for i in range(1,num + 1):
    factorial = factorial * i
print(factorial)