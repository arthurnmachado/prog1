def matrizImpar(M: list, n: int):
	l = c = 0

	for i in range(1, (n**2)+1):
		if c == len(M):
			c = 0
		if l < 0:
			l = len(M)-1

		if M[l][c] == 0:
			if i == 1:
				c = len(M) // 2

		else:
			l = var1 + 1
			c = var2
		M[l][c] = i
		var1 = l
		var2 = c
		l -= 1
		c += 1

	return M


M = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
n = 5

print(matrizImpar(M, n))