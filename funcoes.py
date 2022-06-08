def DigaOi(nome):
	print(f"Oi {nome}")

def Fatorial(k):
	fat = 1
	for i in range(k, 0, -1):
		fat *= i
	return fat

DigaOi("Carlos")
f = Fatorial(5)
print(f)