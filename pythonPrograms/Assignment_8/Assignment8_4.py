from threading import *

upperCount = 0
lowerCount = 0
digitCount = 0


def isUpperLetter(str):
    global upperCount
    for i in str:
        if i.isupper():
            upperCount = upperCount + 1
    threadInfo()
    return upperCount


def isLowerLetter(str):
    global lowerCount
    for i in str:
        if i.islower():
            lowerCount = lowerCount + 1
    threadInfo()
    return lowerCount


def isDigit(str):
    global digitCount
    for i in str:
        if i.isdigit():
            digitCount = digitCount + 1
    threadInfo()
    return digitCount


def threadInfo():
    print("thread name : ", current_thread().getName())
    print("thread id : ", current_thread().ident)


def main():
    str = input("Enter the input string")
    small = Thread(target=isLowerLetter, args=(str,))
    capital = Thread(target=isUpperLetter, args=(str,))
    digit = Thread(target=isDigit, args=(str,))
    small.start()
    capital.start()
    digit.start()

    print("Number of lower letters :", lowerCount)
    print("Number of upper letters :", upperCount)
    print("Number of digits :", digitCount)


if __name__ == "__main__":
    main()
