print("""Quantidade de Parcelas        % de Juros sobre o valor inicial da dívida
1                                      0
3                                      10
6                                      15
9                                      20
12                                     25""")
divida = float(input("Digite o valor da sua divida: "))
quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))
if quantidade_parcelas == 1:
    print(F"Valor da divida: R${divida}")
    print("Valor do juros: 0")
    print("Quantidade de parcelas: 1")
    print(f"Valor da parcela; R${divida}")
elif quantidade_parcelas == 3:
    print(F"Valor da divida: R${divida}")
    juros = round((divida * 0.1),2)
    parcelas = round(((divida + juros)/ quantidade_parcelas),2 )
    print(f"Valor do juros: R${juros}")
    print("Numero de parcelas: 3")
    print(f"Valor da parcela; R${parcelas}")
elif quantidade_parcelas == 6:
    print(F"Valor da divida: R${divida}")
    juros = round((divida * 0.15),2)
    parcelas = round(((divida + juros)/ quantidade_parcelas),2 )
    print(f"Valor do juros: R${juros}")
    print(f"Numero de parcelas: {quantidade_parcelas}")
    print(f"Valor da parcela; R${parcelas}")
elif quantidade_parcelas == 9:
    print(F"Valor da divida: R${divida}")
    juros = round((divida * 0.2),2)
    parcelas = round(((divida + juros)/ quantidade_parcelas),2 )
    print(f"Valor do juros: R${juros}")
    print(f"Numero de parcelas: {quantidade_parcelas}")
    print(f"Valor da parcela; R${parcelas}")
elif quantidade_parcelas == 12:
    print(F"Valor da divida: R${divida}")
    juros = round((divida * 0.25),2)
    parcelas = round(((divida + juros)/ quantidade_parcelas),2 )
    print(f"Valor do juros: R${juros}")
    print(f"Numero de parcelas: {quantidade_parcelas}")
    print(f"Valor da parcela; R${parcelas}")
else:
    print("Opção invalida, reinicie o programa")