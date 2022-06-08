def somaMatriz(l: int, M: list):
	linha = M[l]
	soma = 0.0

	for i in range(len(linha)):
		soma += linha[i]

	return soma

#=================================

def mediaMatriz(l: int, M: list):
	linha = M[l]
	soma = 0

	for j in range(len(linha)):
		soma += linha[j]
	media = soma / len(linha)

	return media

#=================================

def criarMatriz():
	m = n = 12
	M = [[0.0]*n for i in range(m)]

	for i in range(m):
		for j in range(n):
			M[i][j] = float(input())

	return M

#=================================

def main():
	l = int(input())
	oper = input()
	M = criarMatriz()
	if oper == "S":
		print(somaMatriz(l,M))
	else:
		print(mediaMatriz(l,M))

main()