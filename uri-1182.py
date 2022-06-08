def anotarColuna(c: int, M: list):
	coluna = []
	for i in range(12):
		coluna.append(M[i][c])
	return coluna

#=================================

def somaMatriz(c: int, M: list):
	coluna = anotarColuna(c, M)
	soma = 0.0

	for i in range(len(coluna)):
		soma += coluna[i]

	return soma

#=================================

def mediaMatriz(c: int, M: list):
	coluna = anotarColuna(c, M)
	soma = 0

	for j in range(len(coluna)):
		soma += coluna[j]
	media = soma / len(coluna)

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
	c = int(input())
	oper = input()
	M = criarMatriz()
	if oper == "S":
		print(somaMatriz(c,M))
	else:
		print(f"{mediaMatriz(c,M):.1f}")

main()