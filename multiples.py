# Trouve la somme des entiers naturels strictement inférieurs à 1000 et qui sont multiples de 3 ou 5.
total = 0

for i in range(0, 1000, 1):
    if (i%3 == 0) or (i%5 == 0):
        total += i
    else:
        continue

print(total)