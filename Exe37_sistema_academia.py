altura = eval(input("Digite sua altura: "))
peso = int(input("Digite seu peso: "))
codigo = int(input("Digite seu código: "))
sair = int(input("Digite (1) continuar ou (0) sair: "))
maiorAltura = altura
maiorAlturaCodigo = codigo
menorAltura = altura
menorAlturaCodigo = codigo
maiorPeso = peso
maiorPesoCodigo = codigo
menorPeso = peso
menorPesoCodigo = codigo
somaAltura = altura
somaPeso = peso
mediaPeso = 0
mediaAltura = 0
a = 0
while (sair != 0):
	altura = eval(input("Digite sua altura: "))
	peso = int(input("Digite seu peso: "))
	codigo = int(input("Digite seu codigo: "))
	sair = int(input("Digite (1) continuar ou (0) sair: "))	
	
	if (altura > maiorAltura):
		maiorAltura = altura
		maiorAlturaCodigo = codigo 
	else:
		maiorAltura = maiorAltura

	if (altura < menorAltura):
		menorAltura = altura
		menorAlturaCodigo = codigo
	else:
		menorAltura =  menorAltura

	if (peso > maiorPeso):
		maiorPeso = peso
		maiorPesoCodigo = codigo
	else:
		maiorPeso = maiorPeso

	if (peso < menorPeso):
		menorPeso = peso
		menorPesoCodigo = codigo
	else:
		menorPeso = menorPeso

	somaAltura = somaAltura + altura
	somaPeso = somaPeso + peso
	a = a + 1

if (a != 0):
	mediaPeso = float(somaPeso) / (a + 1)
	mediaAltura = float(somaAltura) / (a + 1)
	print(f"O mais magro pesa: {menorPeso} Kg , código: {menorPesoCodigo}")
	print(f"O mais gordo pesa: {maiorPeso} kg , código: {maiorPesoCodigo}")
	print(f"Tamanho do mais baixo: {round(menorAltura,2)}m, código: {menorAlturaCodigo}")
	print(f"Tamanho do mais alto: {round(maiorAltura,2)}m , código: {maiorAlturaCodigo}")
	print(f"Média Peso: {round(mediaPeso,2)} Kg")
	print(f"Média altura: {mediaAltura} metros")