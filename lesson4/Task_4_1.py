

if __name__ == '__main__':
    file = open("test.txt", 'w')
    for i in range(1, 101):
        file.write(f"{i}\t{pow(i, 2)}\t{pow(i, 3)}\n")
    file.close()
