from Assignment_2.Arithmatic import *


def PerformOperation(n1, n2):
    print(Add(n1, n2))
    print(Sub(n1, n2))
    print(Mult(n1, n2))
    print(Div(n1, n2))


if __name__ == '__main__':
    print("Enter first number : ")
    num1 = int(input())
    print("Enter second number : ")
    num2 = int(input())
    PerformOperation(num1, num2)