h = 1
n = 2
h_lista = []
n_lista = []
pergunta = int(input(("Digite o n-ésimo termo: ")))
while n <= pergunta:
    print(" ",h, "/", n, " + ", end="")
    h_lista.append(h)
    n_lista.append(n)
    n += 1

print(f"{h}/{n} => {round((sum(h_lista) / sum(n_lista)),2)}")
