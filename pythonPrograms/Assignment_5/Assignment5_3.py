
def printRecursivePattern(n):
    if n > 0:
        print(n, end=" ")
        printRecursivePattern(n-1)


def main():
    n = int(input("Enter the number :"))
    printRecursivePattern(n)


if __name__ == '__main__':
    main()
