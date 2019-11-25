from threading import *

evenSum = 0
oddSum = 0


def evenElementSum(li):
    global evenSum
    for i in li:
        if i % 2 == 0:
            evenSum = evenSum + i
    return evenSum


def oddElementSum(li):
    global oddSum
    for i in li:
        if i % 2 != 0:
            oddSum = oddSum + i
    return oddSum


def acceptList(n):
    arr = []
    for i in range(n):
        el = int(input("Enter the element"))
        arr.append(el)
    return arr


def main():
    num = int(input("Enter the number of elements"))
    brr = acceptList(num)
    evenlist = Thread(target=evenElementSum, args=(brr,))
    evenlist.start()
    oddlist = Thread(target=oddElementSum, args=(brr,))
    oddlist.start()
    print("Sum of even numbers :", evenSum)
    print("Sum of odd numbers :", oddSum)


if __name__ == "__main__":
    main()
