def trocar(frase: str):
	frase = list(frase)
	frase_att = []

	for i in range(len(frase)):
		letra = ord(frase[i])

		if (letra >= 65 and letra <= 90) or (letra >= 97 and letra <= 122):
			letra += 3
			frase_att.append(chr(letra))
		else:
			frase_att.append(chr(letra))

	return frase_att

#========================================================================

def inverter(frase: list):
	frase_att = []

	for i in range (len(frase)-1,-1, -1):
		frase_att.append(frase[i])

	return frase_att

#========================================================================

def trocarF(frase: list):
	for i in range(len(frase) // 2, len(frase)):
		letra = ord(frase[i])
		letra -= 1
		frase[i] = chr(letra)

	frase = "".join(frase)
	return frase

#========================================================================

def main():
	n = int(input())

	for i in range(n):
		frase = input()
		frase = trocar(frase)
		frase = inverter(frase)
		print(trocarF(frase))

main()