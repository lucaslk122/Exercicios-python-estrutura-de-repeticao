var1 = 0 # [0-25]
var2 = 0 # [26-50]
var3 = 0 # [51-75]
var4 = 0 # out of range 
var4 = 0
num = 1
while  num > 0:
    num = int(input("Digite um numero: "))
    if num <= 25:
        var1 += 1
    elif num <= 50:
        var2 += 1
    elif num <= 75:
        var3 += 1
    else:
        var4 += 1
print(f"Quantidade de numeros  entre 0-25: {var1}")
print(f"Quantidade de numeros  entre 26-250: {var2}")
print(f"Quantidade de numeros  entre 51-75: {var3}")
print(f"Quantidade de numeros fora do range: {var4}")