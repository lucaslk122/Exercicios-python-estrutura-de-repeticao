print("""Sistema eleitoral, esses são os candidatos disponiveis:
[1] Lucas
[2] Sarah
[3] Pedro
[4] Miguel
[5] Voto nulo
[6] Voto Branco
""")
lucas = 0
sarah = 0
pedro = 0
miguel = 0
nulo = 0
branco = 0
num = 1
TotalVotos = 0
while num > 0:
    num = int(input("Coloque o código do seu candidato: "))
    if num == 1:
        lucas += 1
    elif num == 2:
        sarah += 1
    elif num == 3:
        pedro += 1
    elif num == 4:
        miguel += 1
    elif num == 5:
        nulo += 1
    elif num == 6:
        branco += 1
    else:
        print("Opção invalida")
    TotalVotos += 1
print(f"Total de votos {TotalVotos}")
print(f"Votos no candidato Lucas: {lucas}")
print(f"Votos na candidata Sarah: {sarah}")
print(f"Votos na candidata Pedro: {pedro}")
print(f"Votos no candidato Miguel: {miguel}")
print(f"Voto nulo: {nulo}")
print(f"Voto Branco: {branco}")