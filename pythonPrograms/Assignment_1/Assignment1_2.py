def ChkNum(number):
    if number % 2 == 0:
        print("Even Number")
    else:
        print(" Odd Number")


if __name__ == '__main__':
    print("Enter the number : ")
    n = input()
    ChkNum(int(n))