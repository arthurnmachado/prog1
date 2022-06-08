def listar():
	n = int(input())

	listaL = []
	for i in range(n):
		lingua = input()
		listaL.append(lingua)

	return listaL

#================================

def analisar(listaL: list):
	l_var = listaL[0]
	for i in range(len(listaL)):
		if listaL[i] == l_var:
			lingua_usada = listaL[i]
		else:
			lingua_usada = "ingles"
			break

	return lingua_usada

#================================

def main():
	n = int(input())
	for i in range(n):
		listaL = listar()
		print(analisar(listaL))


main()