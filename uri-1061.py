"""dia, diai = input().split()
horai, minutoi, segundoi = map(int, input().split(":"))

dia, diaf = input().split()
horaf, minutof, segundof = map(int, input().split(":"))

diai = int(diai)
diaf = int(diaf)

if diai <= diaf:
	diat = diaf - diai
	if horai <= horaf:
		horat = horaf - horai
		if minutoi <= minutof:
			minutot = minutof - minutoi
			if segundoi <= segundof:
				segundot = segundof - segundoi
			else:
				minutot -= 1
				segundot = (60 - segundoi) + segundof
		else:
			horat -= 1
			minutot = (60 - minutoi) + minutof
			if segundoi <= segundof:
				segundot = segundof - segundoi
			else:
				minutot -= 1
				segundot = (60 - segundoi) + segundof
	else:
		diat -= 1
		horat = (24 - horai) + horaf
		if minutoi <= minutof:
			minutot = minutof - minutoi
			if segundoi <= segundof:
				segundot = segundof - segundoi
			else:
				minutot -= 1
				segundot = (60 - segundoi) + segundof
		else:
			horat -= 1
			minutot = (60 - minutoi) + minutof
			if segundoi <= segundof:
				segundot = segundof - segundoi
			else:
				minutot -= 1
				segundot = (60 - segundoi) + segundof

print(f"{diat} dia(s)")
print(f"{horat} hora(s)")
print(f"{minutot} minuto(s)")
print(f"{segundot} segundo(s)")"""

dia,date1=input().split()
date1 = int(date1)
h1,m1,s1=map(int, input().split(":"))

dia,date2=input().split()
date2 = int(date2)
h2,m2,s2=map(int, input().split(":"))


count_passed_second = (h1*60*60)+(m1*60)+s1
count_remain_second1 = (86400-count_passed_second)
count_remain_second2 = (h2*60*60)+(m2*60)+s2
date = (date2-1)-date1
count_date_second = date*86400
total_second = count_remain_second1+count_remain_second2+count_date_second


D = total_second/86400
total_second = total_second%86400
H = total_second/3600
total_second = total_second%3600
M = total_second/60
total_second = total_second%60
S = total_second

D = int(D)
H = int(H)
M = int(M)
S = int(S)

print(f"{D} dia(s)")
print(f"{H} hora(s)")
print(f"{M} minuto(s)")
print(f"{S} segundo(s)")