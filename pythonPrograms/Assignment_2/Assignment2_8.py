def printPattern(n):
    for j in range(1, n+1):
        print(*range(1, j+1))


if __name__ == '__main__':
    print("Enter the number : ")
    n = int(input())
    printPattern(n)