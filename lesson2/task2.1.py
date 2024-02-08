def LineFromNum(n: int) -> str:
    return "-"*n

def main():
    Num = int(input("Введите N:"))
    print(LineFromNum(Num))

if __name__=='__main__':
  main()
