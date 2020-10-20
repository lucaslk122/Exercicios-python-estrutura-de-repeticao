numero = input("Digite um numero (que contenha mais de 3 digitos): ")
while len(numero) < 3:
    numero = input("Digite um numero (que contenha mais de 3 digitos): ")
print(numero[::-1])
