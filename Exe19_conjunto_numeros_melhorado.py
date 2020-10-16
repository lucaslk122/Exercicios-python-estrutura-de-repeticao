num = int(input("Digite a quantidade de numeros que deseja no conjunto: "))
pergunta = 0
lista = []
while pergunta < num:
    num1 = int(input("Digite um numero: "))
    while num1 < 0 or num1 > 1000:
        print("Numero invalido")
        num1 = int(input("Digite um numero: "))
    pergunta += 1
    lista.append(num1)
print(f"Os numeros digitais foram {lista}")
print(f"O menor valor digitado foi {min(lista)}")
print(f"O maior valor digitado foi {max(lista)}")
print(f"A soma dos valores é {sum(lista)}")