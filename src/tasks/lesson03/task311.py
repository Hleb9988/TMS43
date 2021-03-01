from django.http import HttpRequest
from django.http import HttpResponse

from main.util import render_template

TEMPLATE = "tasks/lesson03/task311.html"

def handler(request: HttpRequest) -> HttpResponse:
    sentence = request.GET.get("sentence", "")
    result = is_gmail(sentence) if sentence else ""

    context = {
        "text": result,
    }

    document = render_template(TEMPLATE, context)

    response = HttpResponse(document)

    return response


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


if __name__ == "__main__":
    print(is_gmail(ask_user()))
