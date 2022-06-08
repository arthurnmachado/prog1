n = int(input())
par = 0
impar = 0

for i in range(n):
  x = int(input())
  if x % 2 == 0:
    par += x
  else:
    impar += x

print(f"Pares: {par}")
print(f"Impares: {impar}")