def printEvenNum():
    count = 1
    n = 1
    while count <= 10:
        if n % 2 == 0:
            print(n)
            count += 1
        n = n + 1


if __name__ == '__main__':
    printEvenNum()
