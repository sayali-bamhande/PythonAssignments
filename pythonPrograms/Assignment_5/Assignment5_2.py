def printRecursivePattern(n):
    if n > 0:
        printRecursivePattern(n-1)
        print(n, end=" ")


def main():
    n = int(input("Enter the number :"))
    printRecursivePattern(n)


if __name__ == '__main__':
    main()
