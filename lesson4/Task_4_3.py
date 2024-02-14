from Task_4_2 import Address
from Task_4_2 import Phone
from enum import IntEnum

class IxType(IntEnum):
    NONE: int = 0
    ADDRESS: int = 1
    PHONE: int = 2

class PhoneBook:
    book: list = []
    index: dict = {}
    indType: int = 0

    def clear(self):
        indType = IxType.NONE
        self.book.clear()
        self.index.clear()

    def __init__(self):
        self.clear()

    def get_item(self, ind: str):
        try:
            p = self.book[self.index[ind.upper()]]
            if (self.indType==IxType.PHONE):
                result = f"Улица:{p.address.street}, дом:{p.address.home}, квартира:{p.address.flat}"
            else:
                result = f"{p.number}"
        except LookupError:
            result = "Не найден"

        return result

    def set_index(self, ind: int):
        if (ind == self.indType):
            return
        self.indType = ind
        self.index.clear()
        if (self.indType > int(IxType.NONE)):
            i = 0
            for p in self.book:
                if(self.indType == int(IxType.ADDRESS)):
                       self.index[f"{p.address.street.upper()} {str(p.address.home).upper()} {str(p.address.flat)}"] = i
                elif (self.indType == int(IxType.PHONE)):
                       self.index[p.number] = i
                i += 1


def load(filename: str) -> PhoneBook:
    pb = PhoneBook()
    fl = []
    with open(filename, 'r') as file:
       fs = file.read()
       if (len(fs)>0):
           fl = fs.split("\n")
           for l in fl:
               if (len(l) > 0):
                   la = l.split("\t")
                   p = Phone()
                   p.address.street = la[0]
                   p.address.home = la[1]
                   p.address.flat = la[2]
                   p.number = la[3]
                   pb.book.append(p)
    return pb

if __name__ == '__main__':
        filename = "phones.txt"
        PB = load(filename)
#        PB.set_index(IxType.PHONE)
        print(f"Адресная книга:'{filename}', загружено записей:{len(PB.book)}")
        print("Поиск по адресной книге")
        it = int(input("Выберите вариант поиска (1 - по адресу, 2 - по номеру телефона):"))
        if (it < 0 or it > 2 ):
            it = 1
        prompt = ""
        if (it == 1):
            prompt = "Введите адрес в формате <Улица Дом Квартира>:"
        else:
            prompt = "Введите номер телефона:"

        s = input(prompt)
        PB.set_index(it)
        print(PB.get_item(s))
