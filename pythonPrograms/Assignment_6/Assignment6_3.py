class Arithmetic:

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self, n1, n2):
        self.value1 = n1
        self.value2 = n2

    def Addition(self):
        return self.value1 + self.value2

    def Subtraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        return self.value1 / self.value2

    def Display(self):
        print("Addition : ", self.Addition())
        print("Subtraction : ", self.Subtraction())
        print("Multiplication : ", self.Multiplication())
        print("Division : ", self.Division())


def main():
    Obj1 = Arithmetic()
    n1 = int(input("Enter the 1st no. : "))
    n2 = int(input("Enter the 2nd no. : "))
    Obj1.Accept(n1, n2)
    Obj1.Display()


if __name__ == "__main__":
    main()
