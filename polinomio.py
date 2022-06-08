def calcular(lista: list, x):
	polinomio = 0

	for i in range(len(lista)):
		polinomio += lista[i] * (x**i)

	return polinomio

#========================================

def main():
	lista = list(map(float, input().split()))
	n = int(input())

	for i in range(n):
		x = float(input())
		polinomio = calcular(lista, x)
		print(f"{polinomio:.4f}")

main()