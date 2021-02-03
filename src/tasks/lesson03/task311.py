def ask_user():
    full_email = input("Введите email: ")
    return full_email


def is_gmail(full_email):
    email = full_email.split('%40')
    if "gmail.com" == email[1]:
        result = full_email
    else:
        result = "DOMAIN NAME is not supported"
    return result


if __name__ == "__main__":
    print(is_gmail(ask_user()))
