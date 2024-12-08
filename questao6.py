def find_square_for_grains(grains):
    if grains < 1:
        raise ValueError("A quantidade de grãos deve ser maior ou igual a 1.")

    count = 1
    square = 1

    while count < grains:
        count *= 2
        square += 1

    return square

print(find_square_for_grains(16))  # Saída: 5
print(find_square_for_grains(1))   # Saída: 1
print(find_square_for_grains(1024))  # Saída: 11
