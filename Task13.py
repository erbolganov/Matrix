# 13) Сформируйте массив L(I, J) с помощью датчика случайных чисел.
#     Увеличить каждый элемент массива в 3 раза и поменяйте знак на противоположный.
#     Массив выведите на экран в виде таблицы.
import random

n = int(input('Enter the row of the matrix: '))
m = int(input('Enter the column of the matrix: '))
L = [[0 for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        L[i][j] = random.randrange(-50, 50)
    print(L[i])
print()
print('Result after multiplying -3')
for i in range(n):
    for j in range(m):
        L[i][j] *= -3
    print(L[i])
