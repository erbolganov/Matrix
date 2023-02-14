# 2) Дан массив, состоящий из 12 двоичных чисел.
#    Удалить элементы, которые встречаются более двух раз
import random

A = []
i = 0
print("Enter value of the list: ")
while i < 12:
    print(f'A[{i}] =', end=" ")
    A.append(int(input()))
    # if (A[i] > 99 or A[i] < 10):
    #     print('Reenter the item')
    #     continue
    i += 1
print(A)
for item in (A):
    if A.count(item) > 2:
        A.remove(item)
print(A)
