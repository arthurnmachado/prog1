def criarMatriz():
	m = n = 12
	M = [[0.0]*n for i in range(m)]

	for i in range(m):
		for j in range(n):
			M[i][j] = float(input())

	return M

#=====================================

def areaSuperior(M: list):
	lista = []
	var = 11
	
	for i in range(5):
		j = i + 1

		while j < var:
			lista.append(M[i][j])
			j += 1

		var -= 1

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
	metade = areaSuperior(M)
	if oper == "S":
		print(f"{somaLista(metade):.1f}")
	else:
		print(f"{mediaLista(metade):.1f}")

main()