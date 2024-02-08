Name: str = input("Введите Ваше имя: ")
Age: int = int(input("Введите Ваш возраст: "))
Year: int = (2024-Age)
if ( Year < 0 or Year >= 2024 ):
    print("Шутите! Столько не живут.")
    exit(1)
Town: str = input("Введите место жительства (город): ")
Country: str = input("Введите страну: ")
print(f"Уважаемый(ая) {Name}! На сегодняшний день Вы проживаете в стране {Country}, в городе {Town} и родились в {Year} (или {Year-1}) году")