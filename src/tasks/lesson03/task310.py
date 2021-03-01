from typing import Dict
from typing import Tuple

from django.http import HttpRequest
from django.http import HttpResponse

from main.util import render_template

TEMPLATE = "tasks/lesson03/task310.html"

def handler(request: HttpRequest) -> HttpResponse:
    money = request.GET.get("sentence", "")
    result = nominal(money)
    # money = parse_decimal(money_raw)

    # result1 = solution1(money)
    # result2 = solution2(money)

    context = {
        "money": result,
    }

    document = render_template(TEMPLATE, context)

    response = HttpResponse(document)

    return response

def ask_user():
    money = input('Введите через точку число: ').split('.')
    return money


def nominal(money):
    if money =='':
        pass
    else:
        money1 = money.split('.')
        f = int(money1[0])
        t = int(money1[1])
        if f >= 10:
            kup_10 = f // 10
            kup_5 = (f - (kup_10 * 10)) // 5
            kop = ((f - (kup_10 * 10) - (kup_5 * 5)) * 100 + t)
            kop_50 = kop // 50
            kop_20 = (kop - (kop_50 * 50)) // 20
            kop_1 = kop - (kop_50 * 50) - (kop_20 * 20)
            result = (f"К выдаче купюры: номинал 10р. - {kup_10} шт., номинал 5р. -  {kup_5} шт.;"
                      f"К выдаче копейки : номинал 50коп. - {kop_50} шт.,"
                      f"номинал 20коп. - {kop_20} шт.,номинал 1коп. - {kop_1} шт."
                      )
        elif f >= 5 and f < 10:
            kup_10 = 0
            kup_5 = f // 5
            kop = ((f - (kup_5 * 5)) * 100 + t)
            kop_50 = kop // 50
            kop_20 = (kop - (kop_50 * 50)) // 20
            kop_1 = kop - (kop_50 * 50) - (kop_20 * 20)
            result = (f"К выдаче купюры: номинал 10р. - {kup_10} шт., номинал 5р. -  {kup_5} шт.;"
                      f"К выдаче копейки : номинал 50коп. - {kop_50} шт.,"
                      f"номинал 20коп. - {kop_20} шт.,номинал 1коп. - {kop_1} шт."
                      )
        else:
            kop = f * 100 + t
            kup_10 = 0
            kup_5 = 0
            kop_50 = kop // 50
            kop_20 = (kop - (kop_50 * 50)) // 20
            kop_1 = kop - (kop_50 * 50) - (kop_20 * 20)
            result = (f"К выдаче купюры: номинал 10р. - {kup_10} шт., номинал 5р. -  {kup_5} шт.;"
                      f"К выдаче копейки : номинал 50коп. - {kop_50} шт.,"
                      f"номинал 20коп. - {kop_20} шт.,номинал 1коп. - {kop_1} шт."
                      )
        return result


if __name__ == "__main__":
    ask = ask_user()
    res = nominal(ask)
    print(res)
