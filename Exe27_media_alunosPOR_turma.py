import math
turmas = int(input("Quantas turmas existem? "))
perguntas = 0
soma = 0
while perguntas < turmas:
    qtd_alunos = int(input("Quantos alunos tem nessa turma?(deve ter menos de 40 alunos): "))
    while qtd_alunos > 40:
        print("A turma deve ter menos de 40 alunos")
        qtd_alunos = int(input("Quantos alunos tem nessa turma?: "))
    soma += qtd_alunos
    perguntas += 1
media = soma / turmas
print(f"A media de alunos por turma é {math.ceil(media)}")