def isNumber(Num: str)-> bool:
    result = False;
    Num = Num.strip()
    permitChars = "0123456789"
    if (Num[0]=="-"):
        Num = Num[1:]
    if (Num != ""):
        dotCount=0
        for n in Num:
            if (n == "." or n == ","):
                dotCount += 1
                if (dotCount > 1):
                    return False
            elif (n not in permitChars):                
                return False

        result = True
        
    return result

class TriangleChecker:
    a: str
    b: str
    c: str
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def is_triangle(self):
        result = "Жаль, но из этого треугольник не сделать."
        if (not isNumber(self.a) or not isNumber(self.b) or not isNumber(self.c)):
            result = "Нужно вводить только числа!"
        else:
            A = float(self.a)
            B = float(self.b)
            C = float(self.c)
            
            if (A < 0.0 or B < 0.0 or C < 0.0):
                result = "С отрицательными числами ничего не выйдет!"           
            elif ((A + B >= C) and (B + C >= A) and (C + A >= B)):
                result = "Ура, можно построить треугольник!"
        return result

if (__name__ == "__main__" ):
    print("TriangleChecker.v1.0")
    A = input ("Введите длину стороны A:")
    B = input ("Введите длину стороны B:")
    C = input ("Введите длину стороны C:")
    tC = TriangleChecker(A,B,C)
    
    print(tC.is_triangle())
