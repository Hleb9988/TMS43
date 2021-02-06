# Ввести предложение. Если число символов в
# предложении кратно 3 - добавить ! к концу строки.
# Вывести строку на экран.
def symbol(sentence):
	if len(sentence)%3 == 0:
		print (f" {sentence} !")
	else:
		print('Не кратно 3')


def main():
	sentence = input()
	symbol(sentence)


main()


