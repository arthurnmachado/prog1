def criarMatriz():
	m = n = 12
	M = [[0.0]*n for i in range(m)]

	for i in range(m):
		for j in range(n):
			M[i][j] = float(input())

	return M

#=====================================

def areaInferior(M: list):
	lista = []

	
	for i in range(7, len(M)):

		for j in range(len(M)-i, i):
			lista.append(M[i][j])


	return lista

#=====================================

def somaLista(lista: list):
	soma = 0

	for i in range(len(lista)):
		soma += lista[i]

	return soma

#=====================================

def mediaLista(lista: list):
	soma = 0

	for i in range(len(lista)):
		soma += lista[i]
	media = soma / len(lista)

	return media

#=====================================

def main():
	oper = input()
	M = criarMatriz()
	metade = areaInferior(M)
	if oper == "S":
		print(f"{somaLista(metade):.1f}")
	else:
		print(f"{mediaLista(metade):.1f}")

main()