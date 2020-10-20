gabarito = []
respostas_aluno = []
notas = []
print("Professor: ")
for i in range(10):
    print("Questão: ", i + 1)
    resposta_certa = gabarito.append(input("Digite a alternativa correta: "))
n_aluno = 1
continuar = True
while continuar != 'n':
    print("Aluno n°", n_aluno, ":")
    respostas_aluno.clear()
    for i in range(10):
        print("Questão: ", i + 1)
        resposta_aluno = respostas_aluno.append(input("Escolha a alternativa: "))
    nota = 0
    for i in range(10):
        if respostas_aluno[i] == gabarito[i]:
            nota += 1
    notas.append(nota)
    continuar = input("Outro aluno vai utilizar o sistema? [s/n] : ")
    n_aluno += 1
print(len(notas), "alunos utilizaram o sistema")
print("Maior nota: ", max(notas))
print("menor nota: ", min(notas))
print(f"A media de notas da turma foi de: {sum(notas) / len(notas)}")
print(notas)