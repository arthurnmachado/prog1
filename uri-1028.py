def MDC(a, b):
  while(b != 0):
    resto = a % b
    a = b
    b = resto
  
  return a
#========================

def main():
	num = int(input())

	for i in range(num):
		x, y = map(int, input().split())
		print(MDC(x, y))

main()