import datetime


def get_friday13(year: int) -> list[datetime]:

    result = list()
    for m in range(1, 12):
        d_str = f"13.{str( m )}.{str( year )}"
        d1 = datetime.datetime.strptime(d_str, "%d.%m.%Y")
        if d1.weekday() == 4:  # пятница
            result.append(d1)
    return result


if __name__ == '__main__':
    y = int(input("Введите год: "))
    lf13 = get_friday13(y)
    if len(lf13) > 0:
        print(f"Список пятниц 13 в {str(y)} году: ")
        for d in lf13:
            print(d.strftime('%d.%m.%Y'))
    else:
        print(f"К сожалению, в {str(y)} году нет пятниц 13")
