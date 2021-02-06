# Задание 3.05
# Ввести предложение. Если в предложении есть слово
# code - вывести на экран Yes, иначе вывести на экран No


def code_in(sentence):
	if "code" in sentence:
		print("Yes")
	else:
		print("No")


def main():
	sentence = input()
	code_in(sentence)


main()


