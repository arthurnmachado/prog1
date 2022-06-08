n = int(input())

maior = 0
menor = 0
for i in range(n):
	y = int(input())
	if maior < y:
		maior = y

	if menor == 0:
		menor = y

	if menor > y:
			menor = y
print(f"Maior = {maior}")
print(f"Menor = {menor}")