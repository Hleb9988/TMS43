# Задания 3.08
# Ввести число, проверить на то, что было введено именно
# число. Возвести его в куб.

def is_num(num):
	if num.isdigit():
		print((int(num))**3)
	else:
		print('Введено не число')


def main():
	num = input()
	is_num(num)


main()
