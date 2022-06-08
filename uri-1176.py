def fibonacci():
  lista = [0, 1]
  for i in range(2, 61):
    num  = lista[i-2] + lista[i-1]
    lista.append(num)

  return lista

#====================================

def printar(n, lista: list):
  for j in range(n):
    x = int(input())
    print(f"Fib({x}) = {lista[x]}")

#====================================

def main():
  lista = fibonacci()
  n = int(input())
  printar(n, lista)
  
main()