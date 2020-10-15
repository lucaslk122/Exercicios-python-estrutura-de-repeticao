nome = input("Digite seu nome(precisa ter mais que 3 caracteres): ")
while len(nome) < 3:
    print("Nome invalido, precisa ter mais que 3 caracteres")
    nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:
    print("Idade invalida, digite novamente")
    idade = int(input("Digite sua idade: "))
sexo = input("Digite seu sexo [m]Masculino ou [F]Feminino: ").lower()
while sexo != "m" != "f":
    print("Sexo invalido, digite novamente")
    sexo = input("Digite seu sexo [m]Masculino ou [F]Feminino: ").lower()
salario = float(input("Digite seu salario(maior que 0) R$: "))
while salario < 0:
    print("Salario invalido,digite um salario maior que 0")
    salario = float(input("Digite seu salario(maior que 0) R$: "))
estadoCivil = input("Seu estado civil [s]Solteiro, [c]Casado, [v]viuvo(a) ou [d]divorciado: ").lower()
while estadoCivil != "s" != "c" != "v" != "d":
    print("Estado civil invalido, digite novmaente")
    estadoCivil = input("Seu estado civil [s]Solteiro, [c]Casado, [v]viuvo(a) ou [d]divorciado: ").lower()
print("Cadastro concluido")