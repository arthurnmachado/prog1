def combinar(x: str, y: str):
	x = list(x)
	y = list(y)
	combinacao = []

	if len(x) <= len(y):
		for i in range(len(x)):
			combinacao.append(x[i])
			combinacao.append(y[i])
		for j in range(len(y) - len(x), len(y)):
			combinacao.append(y[j])

	print(combinacao)
	

combinar("Tpo", "oCder")