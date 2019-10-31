def factorial(n):
    if n == 0:
        return 1
    else:
        for i in range(1, n):
            return n * n-1


if __name__ == '__main__':
    print("Enter the number : ")
    n = int(input())
    print(n, "! : ", factorial(n))