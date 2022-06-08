m = 3
n = 3
A = []
B = []
num = 0

for i in range(m):
	linha = [num] * n
	num += 1
	A.append(linha)

for i in range(m):
	B.append(A)

print(A)
print(B[0][1][0])
