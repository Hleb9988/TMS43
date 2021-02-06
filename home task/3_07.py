# Задание 3.07
# Ввести строку с клавиатуры
# Если длина строки больше 5 - вывести значение на экран
# Если длина строки меньше 5 - вывести строку “Need more!”
# Если длина строки равна 5 - вывести строку “It is five”



def treatment(string):
	if len(string) > 5:
		print(string)
	elif len(string) < 5:
		print("Need more")
	elif len(string) == 5:
		print("It is five")


def main():
	string = input()
	treatment(string)


main()

