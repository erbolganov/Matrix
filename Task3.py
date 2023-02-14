# 3) Задан массив чисел в двоичной системе счисления.
#    Упорядочить элементы массива по убыванию.
#    Определить сумму чисел.
import random

n = int(input('Enter the length of the list: '))
A = []
s = 0  # Summ of list items
for i in range(n):
    b = random.randrange(20)
    A.append(bin(b))
    s += b
print(f'List: {A}')
# print(f'List in binary system: {bin(A)}')
A.sort(reverse=1)
print(f'Max element: {max(A)} \nMin element: {min(A)}')
print(f'Sorted list: {A}')
print(f'Sum of list items: {bin(s)}')
