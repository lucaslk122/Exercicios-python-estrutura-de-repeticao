nota = float(input("Digite uma nota de 0 a 10: "))
while nota > 10 or nota < 0:
    print("Nota invalida, digite novamente")
    nota = float(input("Digite uma nota de 0 a 10: "))
print("Nota válida")
