num = float(input())
count = int(input())
euler = 0

for d in range(count+1):
  k = d
  fatorial = 1
  while k > 0:
    fatorial *= k
    k -= 1

  euler += (num ** d) / fatorial

print(f"{euler:.4f}")