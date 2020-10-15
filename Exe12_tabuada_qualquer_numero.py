print("Programa para calcular qualquer tabuada")
numero = int(input("Digite um numero valido compreendido entre 1 e 10: "))
while numero < 1 or numero > 10:
    print("Intervalo errado, digite novamente")
    numero = int(input("Digite um numero valido compreendido entre 1 e 10: "))
for i in range(0,11):
    x = numero * i
    print(f"{numero}x{i} = {x}")