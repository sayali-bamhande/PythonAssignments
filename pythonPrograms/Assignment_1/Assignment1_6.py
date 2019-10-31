def ChkNum(number):
    if number == 0:
        print("Zero")
    elif number > 0:
        print("Positive Number")
    else:
        print("Negative Number")


if __name__ == '__main__':
    print("Enter the number : ")
    n = input()
    ChkNum(int(n))