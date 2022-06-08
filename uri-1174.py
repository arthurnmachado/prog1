l = []
for i in range(100):
  x = float(input())
  l.append(x)
  if x <= 10:
    print(f"A[{i}] = {l[i]:.1f}")