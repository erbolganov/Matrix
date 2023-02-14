# 12) Дана целочисленная матрица А[n,m]. Посчитать количество элементов
#     матрицы, превосходящих среднее арифметическое значение элементов
#     матрицы. Принять n=4, m=5.
import random

n = int(input('Enter the row of the matrix: '))
m = int(input('Enter the column of the matrix: '))
A = [[0 for i in range(m)] for j in range(n)]
counter = 0
sum = 0
average = 0

for i in range(n):
    for j in range(m):
        A[i][j] = random.randrange(50)
        sum += A[i][j]
    print(A[i])
average = sum / (n * m)
for i in range(n):
    for j in range(m):
        if A[i][j] > average:
            counter += 1
print(f"Average of matrix: {average}")
print(f'{counter} - elements are bigger than average')
