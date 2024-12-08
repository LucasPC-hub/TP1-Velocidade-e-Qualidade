def bubble_sort_strings(strings):

    n = len(strings)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Troca se a string encontrada for maior que a próxima
            if strings[j] > strings[j + 1]:
                strings[j], strings[j + 1] = strings[j + 1], strings[j]


listas_de_strings = [
    ["banana", "maçã", "cereja", "data"],
    ["zebra", "macaco", "maçã", "cachorro"],
    ["abacaxi", "uva", "kiwi", "laranja", "banana"],
]

for lista in listas_de_strings:
    bubble_sort_strings(lista)
    print(f"Lista ordenada: {lista}")
