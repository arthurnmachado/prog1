def transformar(n):
	vet = []


	for num in n:
		vet.append(float(num))

	return vet

#=====================================

def somar(u: list, v: list):
	soma = 0
	for i in range(len(u)):
		soma += u[i] * v[i]

	return soma

#=====================================

def main():
	u = input().split()
	v = input().split()

	vet_u = transformar(u)
	vet_v = transformar(v)
	soma = somar(vet_u, vet_v)

	print(f"{soma:.4f}")

main()