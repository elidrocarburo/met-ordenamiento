numeros = [11, 2, 7, 10, 6, 40]

n = len(numeros)
for i in range(n - 1):
    print(f"\nIteración {i + 1}:")
    for j in range(n - 1 - i):

        print(f"  Comparando {numeros[j]} y {numeros[j + 1]}...", end=" ")
        
        if numeros[j] > numeros[j + 1]:

            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]
            print(f"Intercambiado: {numeros}")
        else:
            print("Sin cambio")
    
    print("Estado de la lista:", numeros)

print("\nLista ordenada:", numeros)