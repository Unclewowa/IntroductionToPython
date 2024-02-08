def OddEvenList( l: list) -> tuple:
    oddList = list()
    evenList = list()
    for n in l:
        if n % 2 == 0:
            evenList.append(n)
        else:
            oddList.append(n)
    return oddList,evenList

def main():
    ln = (1,2,3,4,5,6,7,8,9,10,25,39,17,84,132)
    ol,el = OddEvenList(ln)

    print(ol)
    print(el)

if __name__=='__main__':
  main()
