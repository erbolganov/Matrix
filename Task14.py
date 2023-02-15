# 14) Дана целочисленная матрица размера M × N, элементы которой могут
#     принимать значения от 0 до 100. Различные строки матрицы назовем
#     похожими, если совпадают множества чисел, встречающихся в этих
#     строках. Найти количество строк, похожих на первую строку данной
#     матрицы.
import random

n = int(input('Enter the row of the matrix: '))
m = int(input('Enter the column of the matrix: '))
L = [[0 for i in range(m)] for j in range(n)]
counter = 0
for i in range(n):
    for j in range(m):
        L[i][j] = random.randrange(2)
    print(L[i])
firstRow = []
for i in range(m):
    firstRow.append(L[0][i])
print('\n', 'First row: ', firstRow)
otherRow = []
for i in range(1, n, 1):
    otherRow = []
    for j in range(m):
        otherRow.append(L[i][j])
    if firstRow == otherRow:
        counter += 1
print('\n', counter)
