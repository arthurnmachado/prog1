num = int(input())
pos = True
pi = 0

for i in range(1, num+1, 2):
  if pos:
    pi += 4 / i
    pos = False
  else:
    pi -= 4 / i
    pos = True

print(f"{pi:.4f}")