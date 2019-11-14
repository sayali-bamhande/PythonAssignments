class Demo:
    value = 5

    def __init__(self, n1, n2):
        self.no1 = n1
        self.no2 = n2

    def fun(self):
        print("Inside fun")
        print("no1 : ", self.no1)
        print("no2 : ", self.no2)

    def gun(self):
        print("Inside gun")
        print("no1 : ", self.no1)
        print("no2 : ", self.no2)


def main():
    Obj1 = Demo(11, 21)
    Obj2 = Demo(51, 101)

    Obj1.fun()
    Obj1.gun()
    Obj2.fun()
    Obj2.gun()


if __name__ == "__main__":
    main()
