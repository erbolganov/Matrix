# 9) Дан двумерный массив 7×7. Найти сумму модулей
#    отрицательных нечетных элементов.
import random

s = 0  # sum of negative odd elements
a = [[0 for i in range(7)] for j in range(7)]
for i in range(7):
    for j in range(7):
        a[i][j] = random.randint(-50, 50)
    print(a[i], end=',')
    print()
print('Negative elements: ', end='')
for i in range(7):
    for j in range(7):
        if a[i][j] < 0 and a[i][j] % 2 == 1:
            print(a[i][j], end=', ')
            s += a[i][j]

print()
print(f'sum of negative odd elements: {abs(s)}')
