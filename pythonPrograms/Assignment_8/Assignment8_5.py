from threading import *


def print1to50():
    for i in range(1, 51):
        print(i, end=" ")
    print("\n")


def print50to1():
    for i in range(50, 0, -1):
        print(i, end=" ")
    print("\n")


def main():
    thread1 = Thread(target=print50to1, args=())
    thread2 = Thread(target=print1to50, args=())
    thread1.start()
    thread1.join()
    thread2.start()


if __name__ == "__main__":
    main()
