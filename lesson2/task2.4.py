def Stat4Str(s: str) -> list:
    lw = list(s.split(" "))
    n = 0
    for w in lw:
        n += len(w)
    return (len(lw),n)

def main():
    s0="Привет, как дела?"
    print(Stat4Str(s0))

if __name__=='__main__':
  main()
