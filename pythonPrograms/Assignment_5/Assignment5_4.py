sum = 0


def printRecursiveSum(n):
    global sum
    if n > 0:
        sum = int(n % 10) + sum
        n = n // 10
        printRecursiveSum(n)
    return sum


def main():
    n = int(input("Enter the number :"))
    print("Sum of ", n, " is : ", printRecursiveSum(n))


if __name__ == '__main__':
    main()
