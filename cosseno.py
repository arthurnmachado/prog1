#Meu jeito

"""x = float(input())
k = int(input())

positivo = True
potencia = 0
fatorial = 1
cos = 0

for i in range(1, k+1):
	fatorial *= i
	if i % 2 == 0 or i == 1:
		if positivo:
			cos += (x ** potencia) / fatorial
			potencia += 2
			positivo = False

		else:
			cos -= (x ** potencia) / fatorial
			potencia += 2
			positivo = True

print(f"{cos:.4f}")"""

#Jeito do Higa

x = float(input())
k = int(input())

cos = 0.0
alt = 1
for i in range(0, k+1, 2):
	fat = 1
	for j in range(i, 0, -1):
		fat *= j
	#print(fat)

	cos += ((x**i) / fat) * alt
	alt *= -1

print(f"{cos:.4f}")