def printPattern(n):
    for i in range(1, n):
        pattern = " * "
        print(pattern * n)


if __name__ == '__main__':
    print("Enter the number : ")
    n = int(input())
    printPattern(n)