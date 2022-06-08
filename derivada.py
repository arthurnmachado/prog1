def derivar(lista: list):
	derivada = []
	for i in range(len(lista)):
		if i != 0:
			coef = i * lista[i]
			derivada.append(coef)

	return derivada

#=================================

def printar(lista: list):
	for i in range(len(lista)):
		print(f"{lista[i]:.4f}")

#=================================

def main():
	entrada = list(map(float, input().split()))
	derivada = derivar(entrada)
	printar(derivada)

main()