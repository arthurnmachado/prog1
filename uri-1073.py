num = int(input())

for i in range(1, num+1):
	if i % 2 == 0:
		print(f"{i}^2 =", end=" ")
		i = i ** 2
		print(i)
