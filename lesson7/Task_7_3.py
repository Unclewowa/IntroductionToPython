import datetime
from Task_7_2 import get_friday13

def my_date_info( d: datetime = datetime.datetime.now() ) -> ():

    year = d.year

    # количество дней до Нового года
    r1 = f"Количество дней до Нового года: {str( datetime.datetime(year+1, 1,1)-d )}"

    # Количество дней до пятницы 13-го (будующей до конца года), при наличии
    lf13 = get_friday13(year)
    r2 = ""
    if len(lf13) > 0:
        for d13 in lf13:
            if d13 > d:
                r2 = f"Количество дней до пятницы 13-го (будет {d13.strftime('%d.%m.%Y')}): {str(d13-d)}"
                break

    # Количество дней до лета (при наличии), если уже лето, то можно это сообщить.
    r3 = ""
    if datetime.datetime(year, 8, 31) <= d <= datetime.datetime(year, 6, 1):
        r3 = "Уже лето"
    else:
        summer_start = datetime.datetime(year, 6, 1)
        k = (summer_start - d).days
        if k < 0:
            summer_start = datetime.datetime(year+1, 6, 1)
            k = (summer_start - d).days

        r3 = f"Количество дней до лета ({summer_start.strftime('%d.%m.%Y')}): {k}"

    return r1, r2, r3

if __name__ == '__main__':

    s1, s2, s3 = my_date_info()
    print(s1)
    print(s2)
    print(s3)
