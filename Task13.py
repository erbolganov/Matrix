# 13) Сформируйте массив L(I,J) с помощью датчика случайных чисел.
#     Увеличить каждый элемент массива в 3 раза и поменяйте знак на противоположный.
#     Массив выведите на экран в виде таблицы
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
