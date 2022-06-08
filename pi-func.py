def pi_app(n):
	pos = True
	pi = 0
	
	for i in range(1, n+1, 2):
	  if pos:
	    pi += 4 / i
	    pos = False
	  else:
	    pi -= 4 / i
	    pos = True

	return pi

#===========================

def main():
	num = int(input())
	pi_aprox = pi_app(num)
	print(f"{pi_aprox:.4f}")

#===========================

main()