# 8) Отсортировать по возрастанию элементов
#    последней строки целочисленный двухмерный массив 3×4.
import random

a = []

for i in range(4):
    b = []
    for j in range(3):
        b.append(random.randrange(50))
    a.append(b)
print(a)
a[-1].sort()
print(a)
