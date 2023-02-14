# 10) В матрице А(4-строки,3-столбца) поменять местами
#     наибольшие элементы в первом и третьем столбцах.
import random

a = [[0 for i in range(3)] for j in range(4)]

# giving value of matrix elements by random
for i in range(4):
    for j in range(3):
        a[i][j] = random.randrange(50)
    print(a[i], end='')
    print()

# Finding max elements of 1st and 3rd columns
m1 = a[0][0]
m3 = a[0][2]
for i in range(4):
    if m1 <= a[i][0]:
        m1 = a[i][0]
        mi1 = i
    if m3 <= a[i][2]:
        m3 = a[i][2]
        mi3 = i
print(f'max element in 1st column: {m1} \nmax element in 3rd column: {m3} \n')
a[mi1][0] = m3
a[mi3][2] = m1

# Result
print('Result')
for i in range(4):
    print(a[i])
