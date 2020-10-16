from statistics import  mean
lista = []
resposta = "s"
while resposta == "s":
    temperatura = float(input("Temperatura = "))
    lista.append(temperatura)
    resposta = input("Dseja adicionar mais temperatura? s/n: ").lower()
print(f"Menor temperatura {min(lista)}")
print(f"Maior temperatura {max(lista)}")
print(f"Média de temperaturas {mean(lista)}")
