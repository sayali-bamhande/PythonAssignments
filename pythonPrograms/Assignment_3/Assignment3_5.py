from Assignment_3.MarvellousNum import *


def PrimeSum(list1):
    sum = 0
    for i in range(0, len(list1)):
         sum += list1[i]
    print("Sum of prime no is : ",sum)


def ListPrime(n):
    li = list()
    print("Enter the elements :")
    for j in range(0, n):
        li.append(int(input()))
    PrimeSum(ChkPrime(li))


def main():
    print("Enter the number of element :")
    n = int(input())
    ListPrime(n)


if __name__ == '__main__':
    main()
