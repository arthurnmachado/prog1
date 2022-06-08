def media(notas: list):
	media = 0
	for i in range(len(notas)):
		media += notas[i]
	print(f"media = {media / 2}")

#=======================================

def validar():
	lista = []
	var = 0
	while var < 2:
		nota = float(input())
		if nota >= 0 and nota <= 10:
			var += 1
			lista.append(nota)
		else:
			print("nota invalida")

	media(lista)

#=======================================

def main():
	while True:
		try:
			validar()
			print("novo calculo (1-sim 2-nao)")
			n = int(input())
			if n < 1 or n > 2:
				print("novo calculo (1-sim 2-nao)")
				n = int(input())
			elif n == 2:
				break
		except EOFError:
			break

main()