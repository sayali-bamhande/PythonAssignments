def printPattern(n):
    for j in range(n, 0, -1):
        print(" * " * j)


if __name__ == '__main__':
    print("Enter the number : ")
    n = int(input())
    printPattern(n)
