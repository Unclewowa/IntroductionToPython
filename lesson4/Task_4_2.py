class Address:
    street: str
    home: str
    flat: int

    def __init__(self, s: str = "", h: int = 0, f: int = 0):
        self.street = s
        self.home = h
        self.flat = f

    def __str__(self) -> str:
        return f"{self.street}\t{self.home}\t{self.flat}"


class Phone:
    address: Address
    number: str

    def __init__(self,  num: str = "", s: str = "", h: int = 0, f: int = 0):
        self.address = Address(s, h, f)
        self.number = num

    def __str__(self) -> str:
        return f"{self.address}\t{self.number}"


if __name__ == '__main__':
    file = open()
    count = 10
    print("Заполним телефонную книгу.")
    with open("phones.txt", 'w') as file:
        for i in range(count):
            print(f"Введите запись №{i+1}/{count}")
            street = input("Улица: ")
            home = input("Дом: ")
            flat = int(input("Квартира: "))
            phone = input("Номер телефона: ")
            t = Phone(phone, street, home, flat)
            file.write(f"{t}\n")

