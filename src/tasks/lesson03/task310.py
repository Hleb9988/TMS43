def ask_user():
    money = input('Введите через точку число: ').split('.')
    return money


def nominal(money):
    f = int(money[0])
    t = int(money[1])
    if f // 10 != 0:
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
    print(nominal(ask_user()))
