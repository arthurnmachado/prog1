def substitui(l: list):
  for i in range(len(l)):
    if l[i] <= 0:
      l[i] = 1

#================================

def imprime(x: list):
  for i in range(len(x)):
    print(f"X[{i}] = {x[i]}")

#================================

def main():
  l = []
  for i in range(10):
    l.append(int(input()))

  substitui(l)
  imprime(l)

#================================

main()