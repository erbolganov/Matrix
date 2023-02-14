# 4) Задан массив чисел в двоичной системе счисления. Поменять местами
#    максимальный и минимальный элементы.
import random

n = int(input('Enter the length of the list: '))
A = []
max_el = 0  # Max element
max_in = 0  # index of max element
min_el = 0
min_in = 0
for i in range(n):
    A.append(bin(random.randrange(20)))
print(f'List: {A}')
max_el = max(A)
max_in = A.index(max_el)
min_el = min(A)
min_in = A.index(min_el)
print('max_el: ', max_el)
print('min_el: ', min_el)
A[max_in] = min_el
A[min_in] = max_el
print("List after changeing: ", A)
