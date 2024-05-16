V = [9, 8, 7, 12, 0, 13, 21]

pares = []
impares = []

for num in V:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Números pares:", pares)
print("Números ímpares:", impares)