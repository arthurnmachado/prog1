n = int(input())

#backup
n_bkp = n 

#contar digitos de n
dig = 0

while n > 0:
	n = n // 10 
	dig += 1

#achar inverso
exp = dig - 1
n = n_bkp
inv = 0

while n > 0:
	r = n % 10
	n = n // 10
	inv = inv + r * (10**exp)
	exp -= 1

if inv == n_bkp:
	print("SIM")
else:
	print("NAO")