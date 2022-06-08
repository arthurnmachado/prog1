"""
num = int(input())
soma = 1

for i in range(1, num+1, 1):
	print(i)

	if i != 1:
		divisao = i / 2
		soma += divisao

print(soma)
"""

num = int(input())
soma = 0

for i in range(num, 0, -1):
	soma += 1 / i

print(f"{soma:.4f}")