def entrada():
  lista = []
  for i in range(20):
    num = int(input())
    lista.append(num)

  return lista

#===========================

def trocar(lista: list):
  n = 19
  for j in range(10):
    var = lista[j]
    lista[j] = lista[n]
    lista[n] = var

    n -= 1

  return lista

#===========================

def printar(lista_t: list):
  for i in range(len(lista_t)):
    print(f"N[{i}] = {lista_t[i]}")
  
#===========================

def main():
  lista = entrada()
  lista_t = trocar(lista)
  printar(lista_t)

main()