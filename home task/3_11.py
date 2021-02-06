# Задания 3.11
# Ввести почтовый адрес. Проверить доменной имя. В случае если оно
# gmail.com, вывести на экран имя почтового ящика. Иначе вывести надпись
# “DOMAIN NAME is not supported’


# def is_gmail(full_email):
# 	email = full_email.split('@')
# 	if "gmail.com" == email[1]:
# 		print (f'{full_email}')
# 	else:
# 		print("DOMAIN NAME is not supported")


# def main():
# 	full_email = input("Введите email: ")
# 	is_gmail(full_email)


# main()

def ask_user():
    full_email = input("Введите email: ")
    return full_email


def is_gmail(full_email):
    email = full_email.split('@')
    if "gmail.com" == email[1]:
    	result = full_email
    else:
    	result = "DOMAIN NAME is not supported"
    return result


# def main():
# 	ask_user()
# 	is_gmail(full_email)
# 	print(result)


if __name__ == "__main__":
	print(is_gmail(ask_user()))
