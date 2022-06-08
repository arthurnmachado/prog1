def fatorial(x, y):
	fatx = 1
	faty = 1
	if x != 0:
		for i in range(1, x+1):
			fatx *= i

	if y != 0:
		for j in range(1, y+1):
			faty *= j

	soma = faty + fatx

	return soma

#=========================================

def main():
	while True:
		try:
			entrada = input()

			a,b = entrada.split()
			a = int(a)
			b = int(b)

			print(fatorial(a, b))
		except EOFError as e:
			print(end="")
			break

#=========================================

main()