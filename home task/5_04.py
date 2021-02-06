# Задание 5.04
# Дана целочисленная матрица А[n,m]. Посчитать
# количество элементов матрицы, превосходящих среднее
# арифметическое значение элементов матрицы и сумма
# индексов которых четна.

import random
n = int(input("введи число столбцов: "))
m = int(input("введи число строк: "))

x =[[random.randint(1,9) for i in range(n)] for p in range(m)]
num = 0
sum = 0
index = []
for i in range(len(x)):
	for j in range(len(x[i])):
		sum+=x[i][j]
		num+=1
		if (i+j)%2==0:
			index.append(x[i][j])

ar_sum=sum/num
count_elem=0
for i in index:
	if i>ar_sum:
		count_elem+=1
for row in x:
	print (row)
print(count_elem)
