l = []
x = int(input())

for i in range(10):
  if len(l) == 0:
    l.append(x)
    print(f"N[{i}] = {l[i]}")

  else:
    l.append(x)
    print(f"N[{i}] = {l[i]}")
  x *= 2