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

numeros = [11, 2, 7, 10, 6, 40]

print("Lista inicial:", numeros)
insercion_binaria(numeros)
print("\nLista ordenada:", numeros)
