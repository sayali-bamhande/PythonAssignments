from threading import *

even = []
odd = []


def evenNumbers():
    count = 0
    i = 1
    while count != 10:
        if i % 2 == 0:
            even.append(i)
            count += 1
        i += 1


def oddNumbers():
    count = 0
    i = 1
    while count != 10:
        if i % 2 != 0:
            odd.append(i)
            count += 1
        i += 1


def main():
    t1 = Thread(target=evenNumbers, args=())
    t1.start()

    t2 = Thread(target=oddNumbers(), args=())
    t2.start()
    print("Even Numbers : ", even)
    print("Odd Numbers : ", odd)


if __name__ == "__main__":
    main()
