import random

def gerar_pilha_embaralhada():
    """Gera uma pilha de cartas de espadas (1 a 13) embaralhadas."""
    cartas = list(range(1, 14))  # Cartas de 1 a 13
    random.shuffle(cartas)  # Embaralha as cartas
    return cartas

def ordenar_cartas(pilha_desordenada):
    pilha_ordenada = []

    while pilha_desordenada:
        carta_atual = pilha_desordenada.pop(0)

        inseriu = False
        for i in range(len(pilha_ordenada)):
            if carta_atual < pilha_ordenada[i]:
                pilha_ordenada.insert(i, carta_atual)
                inseriu = True
                break

        if not inseriu:
            pilha_ordenada.append(carta_atual)

    return pilha_ordenada


if __name__ == "__main__":
    cartas_embaralhadas = gerar_pilha_embaralhada()
    print("Pilha desordenada:", cartas_embaralhadas)

    cartas_ordenadas = ordenar_cartas(cartas_embaralhadas)
    print("Pilha ordenada:", cartas_ordenadas)
