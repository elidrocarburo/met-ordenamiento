def insercion_binaria(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        low = 0
        high = i - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > key:
                high = mid - 1
            else:
                low = mid + 1
        
        for j in range(i, low, -1):
            arr[j] = arr[j - 1]
        
        arr[low] = key

        print(f"Iteración {i}: {arr}")

letras = ['c', 'g', 'a', 'q', 'j', 'b']

print("Lista inicial:", letras)
insercion_binaria(letras)
print("\nLista ordenada:", letras)
