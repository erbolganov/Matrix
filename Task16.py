# 16) Дана матрица порядка n×m, все элементы которой различны. В каждой
#     строке выбирается элемент с наименьшим значением, затем среди этих
#     чисел выбирается наибольшее.Указать индексы элемента с найденным
#     значением.
import random

n = int(input('Введите количество строков: '))
m = int(input('Введите количество столбцов: '))

# giving value of matrix
matrix = [[0 for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        matrix[i][j] = random.randrange(100)
    print(matrix[i])

# Finding all min elements in each row
rows = []
for i in range(n):
    rows.append(min(matrix[i]))
print('\nMin elements in each row:', rows)
the_most_min_el = min(rows)
r = 0
c = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == the_most_min_el:
            r = i + 1
            c = j + 1
            break
print(f'The most min element:  matrix[{r}][{c}] = {the_most_min_el}')
