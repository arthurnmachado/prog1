T = int(input())

for n in range(T):
	x, y, m, n = input().split()
	x = int(x)
	y = int(y)
	m = float(m)
	n = float(n)
	
	count = 0
	while x <= y and count <= 100:
		x = int(x + x * m / 100)
		y = int(y + y * n / 100)
		count += 1

	if count > 100:
		print("Mais de 1 seculo.")
	else:
		print(f"{count} anos.")