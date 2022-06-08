def trocar(frase: str):
	frase = list(frase)
	italico = negrito = True

	for i in range(len(frase)):
		if frase[i] == "_":
			if italico:
				frase[i] = "<i>"
				italico = False
			else:
				frase[i] = "</i>"
				italico = True
		elif frase[i] == "*":
			if negrito:
				frase[i] = "<b>"
				negrito = False
			else:
				frase[i] = "</b>"
				negrito = True

	frase = "".join(frase)
	return frase

#===============================

def main():
	while True:
		try:
			frase = input()
			print(trocar(frase))
		except EOFError:
			break

main()