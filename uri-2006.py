tipo = int(input())
cha1, cha2, cha3, cha4, cha5 = map(int, input().split())
count = 0

if cha1 == tipo:
	count += 1

if cha2 == tipo:
	count += 1

if cha3 == tipo:
	count += 1

if cha4 == tipo:
	count += 1

if cha5 == tipo:
	count += 1

print(count)