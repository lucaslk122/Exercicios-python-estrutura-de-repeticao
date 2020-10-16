print("Nessa eleição existem 3 candidatos")
total = int(input("Quantos eleitores votaram? "))
perguntas = 0
a = 0
b = 0
c = 0
i = 0
print("Digite 1 para o candidato A, 2 para o B e 3 para o C")
while perguntas < total:
    opção = int(input("Sua opção: "))
    if opção == 1:
        a += 1
    elif opção == 2:
        b += 1
    elif opção == 3:
        c += 1
    else:
        print("Opção invalida")
        i += 1
    perguntas += 1
print(f"Total de votos do candidato A = {a}")
print(f"Total de votos do candidato B = {b}")
print(f"Total de votos do candidato C = {c}")
print(f"Total de votos invalidos = {i}")


    