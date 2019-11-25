from threading import *

evenSum = 0
oddSum = 0


def findFactors(n):
    factors = [1, n]
    for i in range(2, n-1):
        if n % i == 0:
            factors.append(i)
    return factors


def evenFactorsSum(n):
    global evenSum
    f = findFactors(n)
    for i in f:
        if i % 2 == 0:
            evenSum = evenSum + i
    return evenSum


def oddFactorsSum(n):
    global oddSum
    f = findFactors(n)
    for i in f:
        if i % 2 != 0:
            oddSum = oddSum + i
    return oddSum


def main():
    num = int(input("Enter the number"))
    t1 = Thread(target=evenFactorsSum, args=(num,))
    t1.start()
    t2 = Thread(target=oddFactorsSum, args=(num,))
    t2.start()
    print("Sum of Even factors ", evenSum)
    print("Sum of odd factors ", oddSum)


if __name__ == "__main__":
    main()
    print("Exit from main")
