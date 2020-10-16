print("Bem vindo a panificadora do Sr Manoel Joaquim.")
print("A quantidade de itens precia estar compreendida entre 1 e 50")
qtd_itens = int(input("Qual a quantidade de paes?: "))
preço_paes = float(input("Quanto custa o pão? "))
while qtd_itens < 1 or  qtd_itens > 50:
    print("Quantidade invalida")
    qtd_itens = int(input("Qual a quantidade de itens?: "))
totalApagar = qtd_itens * preço_paes
print(f"Voce pagará R${round(totalApagar,2)} por {qtd_itens} paes")