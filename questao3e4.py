def busca_linear(array, alvo):
    passos = 0
    for i in array:
        passos += 1
        if i == alvo:
            print(f"Busca Linear: Passo {passos}, carta = {i}")
            return passos
    return passos

def busca_binaria(array, alvo):
    inicio, fim = 0, len(array) - 1
    passos = 0

    while inicio <= fim:
        passos += 1
        meio = (inicio + fim) // 2
        print(f"Busca Binária: Passo {passos}, índice = {meio}, carta = {array[meio]}")

        if array[meio] == alvo:
            return passos
        elif array[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return passos


# Exemplo de uso
if __name__ == "__main__":
    array_ordenado = [2, 4, 6, 8, 10, 12, 13]
    alvo = 8

    print("== Busca Linear ==")
    passos_linear = busca_linear(array_ordenado, alvo)

    print("\n== Busca Binária ==")
    passos_binaria = busca_binaria(array_ordenado, alvo)

    print(f"\nResultado Final:")
    print(f"Passos na busca linear: {passos_linear}")
    print(f"Passos na busca binária: {passos_binaria}")
