# Задание 5.01
# Создать квадратную матрицу размерностью n
# и заполнить ее случайными значениями от 1
# до 9.

import random
n = int(input("введи число: "))
m = int(input("введи число: "))

x =[[random.randit(1,9) for i in range(n)] for p in range(m)]
for row in x:
	print(row)
