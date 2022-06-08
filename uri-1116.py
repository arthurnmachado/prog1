def dividir(x: int, y: int):
	if y == 0:
		print("divisao impossivel")
	else:
		divisao = x / y
		print(f"{divisao:.1f}")

#======================================

def main():
	n = int(input())

	for i in range(n):
		x, y = map(int, input().split())
		divisao = dividir(x, y)

main()