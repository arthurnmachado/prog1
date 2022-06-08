for i in range(1, 101):
	x = int(input())
	if i == 1:
		maior = x
		num = i

	elif maior < x:
		maior = x
		num = i

print(maior)
print(num)