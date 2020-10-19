maior = menor = count = soma_veiculos = soma_acidentes = soma_2k = 0
cid_maior = cid_menor = 0

for i in range(1,6):
    codigo = int(input("Digite o código da cidade: "))
    veiculos = int(input("Numero de veiculos de passeio: "))
    acidentes = int(input("Numero de acidentes de transito com vitimas: "))

    soma_veiculos += veiculos
    soma_acidentes += acidentes

    if acidentes > maior:
        maior = acidentes
        cid_maior = codigo

    if acidentes < menor or i == 1:
        menor = acidentes
        cid_menor = codigo

    if veiculos < 2000:
        soma_2k += acidentes
        count += 1


media_nas_5_cidades = soma_veiculos / i
media_2k = soma_2k / count

print(f"O menor indice de acidentes de transito é {menor} pertencente a cidade com idnice {cid_menor}")
print(f"O maior indice de acidenstes de transito é {maior} pertencente a cidade com idnice {cid_maior}")
print(f"Media de veiculos nas cincos cidades {media_nas_5_cidades}")
print(f"Media de acidentes de transitos nas cidades com menos de 2000 é {media_2k}") 
