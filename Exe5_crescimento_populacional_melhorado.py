nome1 = input("Digite o nome do seu páis: ")
população1 = int(input("Digite o valor inicial da população: "))
TaxaPop1 = float(input("Digite a taxa de crescimento dessa população: ")) / 100
nome2 = input("Digite o nome do seu páis: ")
população2 = int(input("Digite o valor inicial da população: "))
TaxaPop2 = float(input("Digite a taxa de crescimento dessa população: ")) /100
anos = 0
while população1 <= população2:
    população1 = população1 + (população1*TaxaPop1)
    população2 = população2 + (população2*TaxaPop2)
    anos += 1
print(f"O páis {nome1} ultrapassara o páis {nome2} em {anos} anos")
