nome = input("Digite seu nome: ")
senha = input("Digite sua senha (ela não pode ser igual seu nome): ")
while nome == senha:
    print("senha invalida,tente novamente")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha (ela não pode ser igual seu nome): ")
print("Senha e nome cadastrados com sucesso")