# Задание 3.06
# Запросить у пользователя возраст. Если возраст меньше
# 0 - вывести Wrong input, если меньше 18 - вывести
# CocaCola, иначе - вывести Beer 


def old(age):
	age = int(input("Введите возраст: "))
	if age < 0:
		print("Wrong input")
	elif 0<age<18:
		print("CocaCola")
	else:
		print("Beer")


def main():
	age = int(input("Введите возраст: "))
	old(age)


main()


