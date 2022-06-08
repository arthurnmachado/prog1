variaveis = [1.0, 2.0, 3.0]
num = 0.0

while num < 1.8:
    if num == 0:
        for j in range(3):
            print(f"I={int(num)} J={int(variaveis[j])}")
            variaveis[j] += 0.2
    elif num == 1:
        variaveis[0] = 2
        for j in range(3):
            print(f"I={int(num)} J={int(variaveis[j])}")
            variaveis[j] += 0.2

    else:
        for j in range(3):
            print(f"I={num:.1f} J={variaveis[j]:.1f}")
            variaveis[j] += 0.2
    num += 0.2

num = int(num)
num += 1
for j in range(3):
    print(f"I={int(num)} J={int(variaveis[j])}")