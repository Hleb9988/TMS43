# Задание 5.02
# Создать квадратную матрицу размерностью n
# и заполнить ее случайными значениями.
# Найти сумму всех элементов матрицы,
# которые кратны 3.

import random
n = int(input("введи число: "))
m = int(input("введи число: "))

x =[[random.randint(1,9) for i in range(n)] for p in range(m)]
sum = 0
for i in range(len(x)):
	for j in range(len(x[i])):
		if x[i][j] % 3 == 0:
			sum+=x[i][j]
for row in x:
	print(row)
print(sum)