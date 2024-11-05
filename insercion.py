numeros = [11, 2, 7, 10, 6, 40]

print("Lista inicial:", numeros)

for i in range(1, len(numeros)):
    key = numeros[i]
    j = i - 1

    while j >= 0 and numeros[j] > key:
        numeros[j + 1] = numeros[j]
        j -= 1

    numeros[j + 1] = key
    print(f"Iteración {i}: {numeros}")

print("\nLista ordenada:", numeros)
