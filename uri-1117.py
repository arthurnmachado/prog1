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

validar()