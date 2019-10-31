def ChkNum(number):
    if number % 5 == 0:
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    print("Enter the number : ")
    n = input()
    ChkNum(int(n))