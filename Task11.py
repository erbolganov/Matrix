# 11) Дан двухмерный массив 5×6.
#     Определить среднее арифметическое каждого столбца,
#     определить максимум и минимум каждой строки.
import random

matrix = [[0 for i in range(5)] for j in range(6)]
average = []

# giving value of matrix elements by random
for i in range(6):
    for j in range(5):
        matrix[i][j] = random.randrange(50)
    print(matrix[i], end='')
    print()
print()

# Среднее арифметическое по столбцам
for i in range(5):
    sum = 0
    for j in range(6):
        sum += matrix[j][i]
    average.append(sum / 6)
    # print(sum / 6)
print(f'Среднее арифметическое по столбцам:\n{average}')

# максимум и минимум каждой строки
for i in range(6):
    max_el = max(matrix[i])
    min_el = min(matrix[i])
    print(f'Max: a[{i}] = {max_el}   Min: a[{i}] = {min_el}')
