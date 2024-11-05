letras = ['c', 'g', 'a', 'q', 'j', 'b']

l = len(letras)
for i in range(l - 1):
    print(f"\nIteración {i + 1}:")
    for j in range(l - 1 - i):

        print(f"  Comparando {letras[j]} y {letras[j + 1]}...", end=" ")
        
        if letras[j] > letras[j + 1]:

            letras[j], letras[j + 1] = letras[j + 1], letras[j]
            print(f"Intercambiado: {letras}")
        else:
            print("Sin cambio")
    
    print("Estado de la lista:", letras)

print("\nLista ordenada:", letras)