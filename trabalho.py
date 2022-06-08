def binario(dec):
  binario = 0
  exp = 0
  
  while dec != 0:
    r = dec % 2
    dec = dec // 2
    binario = binario + r * 10 ** exp
    exp += 1

  return binario

#================================================

def contar(bin):
  lista = [0, 0, 0, 0, 0, 0, 0, 0]
  for i in range(len(lista)):
    r = bin % 10
    if r != 0:
      lista[i] += 1
    bin = bin // 10

  return lista
#===============================================

def contarInstrucoes(lista: list):
  count = 0
  for i in range(len(lista)):
    if lista[i] == 1:
      count += 1

  return count

#===============================================

def checkNome(lista: list):
  maior, menor, inutil1, inutil2 = exigencia(lista)
  maiorN = maior
  menorN = menor
  if maior == lista[0]:
    maior = "parafusar capo"
  elif maior == lista[1]:
    maior = "parafusar tampa do porta-malas"
  elif maior == lista[2]:
    maior = "parafusar eixos"
  elif maior == lista[3]:
    maior = "parafusar rodas"
  elif maior == lista[4]:
    maior = "parafusar motor"
  elif maior == lista[5]:
    maior = "parafusar portas"
  elif maior == lista[6]:
    maior = "parafusar chassi"
  elif maior == lista[7]:
    maior = "parafusar assoalho"
  if menor == lista[0]:
    menor = "parafusar capo"
  elif menor == lista[1]:
    menor = "parafusar tampa do porta-malas"
  elif menor == lista[2]:
    menor = "parafusar eixos"
  elif menor == lista[3]:
    menor = "parafusar rodas"
  elif menor == lista[4]:
    menor = "parafusar motor"
  elif menor == lista[5]:
    menor = "parafusar portas"
  elif menor == lista[6]:
    menor = "parafusar chassi"
  elif menor == lista[7]:
    menor = "parafusar assoalho"

  return maior, menor, maiorN, menorN

#===============================================

def exigencia(lista: list):
  mais = 0
  menos = 0
  for i in range(len(lista)):
    if lista[i] >= mais or i == 0:
      mais = lista[i]
      mais_index = i
    if lista[i] <= menos or i == 0:
      menos = lista[i]
      menos_index = i
  return mais, menos, mais_index, menos_index

#===============================================

def addLista(lista1: list, lista2: list):
  for i in range(len(lista1)):
    lista1[i] += lista2[i]

  return lista1

#===============================================

def compararIndex(n, lista: list):
  valor = lista[n]

  return valor

#===============================================

def decimal(binario):
  exp = 0
  dec = 0

  while binario != 0:
    r = binario % 10
    binario = binario // 10
    dec = dec + r * 2 ** exp
    exp += 1
  
  return dec

#===============================================

def printar(listaIns: list, maior, menor, mais, menos, nomeMaior, nomeMenor, maiorN, menorN):
  print(f"1. parafusar capo: {listaIns[0]}.")
  print(f"2. parafusar tampa do porta-malas: {listaIns[1]}.")
  print(f"3. parafusar eixos: {listaIns[2]}.")
  print(f"4. parafusar rodas: {listaIns[3]}.")
  print(f"5. parafusar motor: {listaIns[4]}.")
  print(f"6. parafusar portas: {listaIns[5]}.")
  print(f"7. parafusar chassi: {listaIns[6]}.")
  print(f"8. parafusar assoalho: {listaIns[7]}.")
  print(f"A tarefa mais realizada foi {nomeMaior}: {maiorN} vezes.")
  print(f"A tarefa menos realizada foi {nomeMenor}: {menorN} vezes.")
  print(f"A instrucao que exigiu menos tarefas simultaneas do robo foi a {menor}: {menos} tarefas.")
  print(f"A instrucao que exigiu mais tarefas simultaneas do robo foi a {maior}: {mais} tarefas.")

#===============================================

def main():
  contadorFixo = [0, 0, 0, 0, 0, 0, 0, 0]
  contadorVar = []
  listaExig = []
  listaInput =  []

  while True:
    n = int(input())
    if n == 0:
      break
    else:
      n = binario(n)
      listaInput.append(n)
      nList = contar(n)

      contadorVar = contar(n)
      contadorFixo = addLista(contadorFixo, contadorVar)


      nCount = contarInstrucoes(nList)
      listaExig.append(nCount)

  mais, menos, mais_index, menos_index = exigencia(listaExig)
  maior = compararIndex(mais_index, listaInput)
  maior = decimal(maior)
  menor = compararIndex(menos_index, listaInput)
  menor = decimal(menor)

  nomeMaior, nomeMenor, maiorN, menorN = checkNome(contadorFixo)

  printar(contadorFixo, maior, menor, mais, menos, nomeMaior, nomeMenor, maiorN, menorN)





























































































































































































































































main()