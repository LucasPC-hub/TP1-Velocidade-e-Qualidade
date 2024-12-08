def bubble_sort(numeros):
    n = len(numeros)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numeros[j] > numeros[j + 1]:
                numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]


listas_de_teste = [
    [64, 34, 25, 12, 22, 11, 90],
    [5, 1, 4, 2, 8],
    [3, 0, 2, 5, -1, 4, 1],
]

for lista in listas_de_teste:
    bubble_sort(lista)
    print(f"Lista ordenada: {lista}")
