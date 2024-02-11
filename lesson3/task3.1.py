class Soda:
    addition: str
    
    def __init__(self, component: str = "" ):
        self.addition = component;
            
    def show_my_drink(self):
        if (self.addition == ""):
            print("Обычная газировка.")
        else:
            print(f"Газировка c добавкой: {self.addition}")
    
if (__name__ == "__main__" ):
    print("Газ-Вода-Сироп.v1.0")
    component = input("Введите название добавки: ")
    drink = Soda(component)
    drink.show_my_drink()
