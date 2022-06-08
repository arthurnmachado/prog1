x = int(input())
lista = input().split()
vet = []
dado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for num in lista:
	vet.append(int(num))

for i in range(len(vet)):
	if vet[i] in dado:
		if vet[i] != vet[i-1] or i == 0:
			count = vet.count(vet[i])
			porcentagem = 100 * (count / x)
		
			if i == 0:
				print(f"Face 1: {porcentagem:.2f}%")
			else:
				print(f"Face {vet[i]}: {porcentagem:.2f}%")
	else:
		porcentagem = 0
		print(f"Face {dado[i]}: {porcentagem:.2f}%")
