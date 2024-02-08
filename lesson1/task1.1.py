print("Простой калькулятор v1.0")
Op_A = float(input("Введите первое число: "))
Op_B = float(input("Введите второе число: "))
Op = input("Введите операцию [+-*/]: ")
OpList: list[str]= ['+','-','*','/']
if Op in OpList:
    Res = 0.0
    if Op == "+":
        Res = Op_A + Op_B
    elif Op == "-" :
        Res = Op_A - Op_B
    elif Op == "*" :
        Res = Op_A * Op_B
    elif Op == "/" :
        if Op_B != 0.0 :
            Res = Op_A / Op_B
        else:
            print("Делить на ноль нельзя!")
            exit(1)
    print(f"{Op_A}{Op}{Op_B}={Res}")
else:
    print("Неизвестная операция")