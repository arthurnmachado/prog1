N = int(input())

for i in range(N):
	x, y, z = map(float, input().split())
	media = ((x*2) + (y*3) + (z*5)) / 10
	print(f"{media:.1f}")