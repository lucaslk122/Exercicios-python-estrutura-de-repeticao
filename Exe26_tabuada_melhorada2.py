num = int(input("Montar a tabuada de: "))
comeco = int(input("Começar por: "))
final = int(input("Terminar em: "))
for i in range(comeco,final + 1):
    resul = num * i
    print(f"{num}x{i} = {resul}")