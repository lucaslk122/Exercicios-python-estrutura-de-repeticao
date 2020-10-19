print("""O cardápio da lanchonete é o seguinte:
Especificação        Código  Preço
Cachorro Quente       100     R$ 1,20
Bauru Simples         101     R$ 1,30
Bauru com ovo         102     R$ 1,50
Hambúrguer            103     R$ 1,20
Cheeseburguer         104     R$ 1,30
Refrigerante          105     R$ 1,00
""")
pergunta = 's'
conta = 0
while pergunta == 's':
    codigo = int(input("Digite o codigo do produto: "))
    quantidade = int(input("Digite a quantidade: "))
    if codigo == 100:
        conta += (quantidade*1.20)
    elif codigo == 101:
        conta += (quantidade*1.30)
    elif codigo == 102:
        conta += (quantidade*1.50)
    elif codigo == 103:
        conta += (quantidade*1.20)
    elif codigo == 104:
        conta += (quantidade*1.30)
    elif codigo == 105:
        conta += (quantidade*1)
    else:
        print("Código invalido")
    pergunta = input("Deseja adicionar mais itens ao seu pedido? s/n: ").lower()
print(f" Valor total da compra: R${conta}")