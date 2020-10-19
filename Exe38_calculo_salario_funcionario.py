"""
salario = 1000 + (1000 * 0.015) #ganho em 1996
ano = 1997
while ano < 2020:
    salario = salario + (salario*(0.015*2))
    ano += 1
print(round(salario,2))
"""

#Modificado
salario = float(input("Digite seu salario: "))
ano = 1997
salario = salario + (salario * 0.015)
while ano < 2020:
    salario = salario + (salario*(0.015*2))
    ano += 1
print(round(salario,2))