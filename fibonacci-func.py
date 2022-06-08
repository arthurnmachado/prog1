def maiorQueDois(n):
	if n == 0 or n == 1:
		fib = n

	else:
		a = 0
		b = 1
		for i in range(n-1):
			fib = a + b
			a = b
			b = fib

		return fib
#=========================

num = int(input())



print(maiorQueDois(num))