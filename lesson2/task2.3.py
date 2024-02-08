def SepStr(s: str, sep: str) -> str:
    l = list(s)
    result = ""
    i = 0
    for c in l:
        if i>0:
            result += sep
        result += c
        i += 1
    return result

def main():
    s_="Привет"
    sep_="-*-"
    print(SepStr(s_,sep_))

if __name__=='__main__':
  main()
