print("Bem vindo a lojas de artigos do Sr Manoel Joaquim. Todos os produtos desta loja custam R$1.99")
print("A quantidade de itens precia estar compreendida entre 1 e 50")
qtd_itens = int(input("Qual a quantidade de itens?: "))
while qtd_itens < 1 or  qtd_itens > 50:
    print("Quantidade invalida")
    qtd_itens = int(input("Qual a quantidade de itens?: "))
totalApagar = qtd_itens * 1.99
print(f"Voce pagará R${round(totalApagar,2)} por {qtd_itens} itens")