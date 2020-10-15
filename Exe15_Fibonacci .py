ultimo = 1
penultimo = 1
conta = 1
print(ultimo)
print(penultimo)
while conta <= 9:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        conta += 1
        print(termo,end=" ")