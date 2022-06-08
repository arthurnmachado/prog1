pizza, adicional, borda = input().split()

if pizza == "P":
  soma = 15.00

elif pizza == "M":
  soma = 18.50

else:
  soma = 23.00

while True:
  if adicional == "S":
    if pizza == "P":
      soma += 2.5
      if borda == "S":
        soma += 5
        print(f"Total: R$ {soma:.2f}")
        break
      else: 
        print(f"Total: R$ {soma:.2f}")
        break
    else:
      soma += 4
      if borda == "S":
        soma += 5
        print(f"Total: R$ {soma:.2f}")
        break
      else: 
        print(f"Total: R$ {soma:.2f}")
        break
  elif borda == "S":
    soma += 5
    print(f"Total: R$ {soma:.2f}")
    break
  else:
    print(f"Total: R$ {soma:.2f}")
    break