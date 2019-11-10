fact = 1


def factorialRecursive(n):
    global fact
    if n > 0:
        factorialRecursive(n - 1)
        fact = n * fact
    return fact


def main():
    n = int(input("Enter the number :"))
    print("Factorial of ", n, " is : ", factorialRecursive(n))


if __name__ == '__main__':
    main()
