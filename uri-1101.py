while True:
  m, n = map(int, input().split())
  
  if m <= 0 or n <= 0:
    break
  else:
    if m > n:
      maior = m
      menor = n
    else:
      maior = n
      menor = m
    soma = 0
    for menor in range(menor, maior+1, 1):
      soma += menor
      print(menor, end=" ")
    print(f"Sum={soma}")