def formarList(n):
  lista = []
  while True:
    for i in range(n):
      lista.append(i)
      if len(lista) >= 1000:
        break
    if len(lista) >= 1000:
      break
    
  return lista

#===================================

def printar(lista: list):
  for k in range(len(lista)):
    print(f"N[{k}] = {lista[k]}")

#===================================

def main():
  t = int(input())
  lista = formarList(t)
  
  printar(lista)

main()