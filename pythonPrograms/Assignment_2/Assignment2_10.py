def getDigitAddition(n):
    sum = 0
    while n > 0:
        sum = n % 10 + sum
        n = int(n / 10)
    return sum


if __name__ == '__main__':
    print("Enter the number : ")
    n = int(input())
    print(getDigitAddition(n))
