a = 0
b = 0
maiorAluno = 0
menorAluno = 1000

for i in range(1, 11):
    num = int(input("Digite o número do aluno: "))
    altura = int(input("Digite a altura do aluno em centímetros: "))    
    if (altura > maiorAluno):
        maiorAluno = altura
        a = num
    if (altura < menorAluno):
        menorAluno = altura
        b = num
        
print(f"Número do aluno mais alto é: {a}, tem: {maiorAluno} cm")
print(f"Número do aluno mais baixo é: {b}, tem: {menorAluno} cm")