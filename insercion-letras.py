letras = ['c', 'g', 'a', 'q', 'j', 'b']

print("Lista inicial:", letras)

for i in range(1, len(letras)):
    key = letras[i]
    j = i - 1

    while j >= 0 and letras[j] > key:
        letras[j + 1] = letras[j]
        j -= 1

    letras[j + 1] = key
    print(f"Iteración {i}: {letras}")

print("\nLista ordenada:", letras)