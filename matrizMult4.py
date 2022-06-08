def geraMatriz4m(M: list):
	j = 1
	k = 0

	for i in range(len(M)):
		k = 0
		while k < len(M):
			M[i][k] = j
			j += 1
			k += 1

	return M

def matriz4m(M: list, n: int):
	M = geraMatriz4m(M)
	l = 0
	c = 0
	
	for i in range(n//4):
		varM = M[i*4]
		print(varM)
		break
		for j in range(len(varM)):
			print("oi")


M = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
n = 4
M = geraMatriz4m(M)
matriz4m(M,n)
