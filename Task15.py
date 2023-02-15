# 15) Дана матрица размера 5×10. Вывести количество столбцов, элементы
#     которых монотонно убывают.
import random

n = int(input('Введите количество строков: '))
m = int(input('Введите количество столбцов: '))
matrix = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = random.randrange(100)
    print(matrix[i])

counter = 0  # количество столбцов
for j in range(m):
    el = 0  # количество элементы которых монотонно убывают
    for i in range(n - 1):
        if matrix[i][j] > matrix[i + 1][j]:
            el += 1
    if el == (n - 1):
        counter += 1
print('\nколичество столбцов которых монотонно убывают', counter)
