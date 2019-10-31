def Add(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    print("Enter 1st number : ")
    n1 = int(input())
    print("Enter 2nd number : ")
    n2 = int(input())
    result = Add(n1, n2)
    print("Addition is : ", result)
