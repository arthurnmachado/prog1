n = int(input())

if n == 0 or n == 1:
	soma = n

else:
	x = 0
	y = 1

	for i in range(n-1):
		soma = x + y
		x = y
		y = soma

print(soma)