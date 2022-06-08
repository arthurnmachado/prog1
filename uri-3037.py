def inputar():
  mariaN = 0
  joaoN = 0

  for j in range(3):
    joao = list(map(int, input().split()))
    joao = joao[0] * joao[1]
    joaoN += joao

  for i in range(3):
      maria = list(map(int, input().split()))
      maria = maria[0] * maria[1]
      mariaN += maria

  return mariaN, joaoN

#=====================================

def main():
  n = int(input())

  for i in range(n):
    mariaN, joaoN = inputar()
    if mariaN > joaoN:
      print("MARIA")
    else:
      print("JOAO")

main()