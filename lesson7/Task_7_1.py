import datetime


def d_weeks_after(date_str: str, weeks: int = 1) -> str:
    return (datetime.datetime.strptime(date_str, "%d.%m.%Y") + datetime.timedelta(weeks=weeks)).strftime('%d.%m.%Y')


if __name__ == '__main__':
    nw = 1
    d_str = input(f"Введите дату в формате День.Месяц.Год: ")
    print(f"Через {nw} неделю/ь/и после {d_str} будет {d_weeks_after(d_str, nw)}\n")
