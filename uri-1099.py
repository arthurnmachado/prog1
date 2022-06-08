num = int(input())
count = 0

for count in range(count, num, 1):
  a, b = map(int, input().split())
  if a > b:
    maior = a
    menor = b
  else:
    maior = b
    menor = a
  menor += 1
  soma = 0
  while menor < maior:
    if menor % 2 != 0:
      soma += menor
    menor += 1
  print(soma)