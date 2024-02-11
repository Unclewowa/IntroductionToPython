from math import pi as PI

class piNum:
    accuracy: int
    cur_pi: str        
        
    def set_pi_prec(self, accuracy):
        if (accuracy > 5):
            accuracy = 5
        elif (accuracy < 2):
            accuracy = 2
        self.accuracy = accuracy
        self.cur_pi = self.__max_pi[:accuracy+2]
    
    def __init__(self, accuracy: int = 2):
        self.__max_pi = str(PI)[:15]
        self.set_pi_prec(accuracy)
    
    def __str__(self):
        return self.cur_pi
    
    def getMaxPi(self):
        return self.__max_pi
    

if (__name__ == "__main__" ):
    print("Pi accuracy calculator v.1.0")  
    nPi = piNum(3)
    print(nPi)
    nPi.set_pi_prec(5)
    print(nPi)
    print(nPi.getMaxPi())
