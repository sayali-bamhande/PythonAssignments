class Circle:
    pi = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self, r):
        print("Inside Accept")
        self.radius = r

    def CalculateCircumference(self):
        self.circumference = 2 * self.radius * self.pi

    def CalculateArea(self):
        self.area = self.radius * self.radius * self.pi

    def Display(self):
        print("radius : ", self.radius)
        print("area of Circle : ", self.area)
        print("circumference of circle : ", self.circumference)


def main():
    Obj1 = Circle()
    rad = int(input("Enter radius of circle : "))
    Obj1.Accept(rad)
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()

    Obj2 = Circle()
    rad = int(input("Enter radius of circle : "))
    Obj2.Accept(rad)
    Obj2.CalculateArea()
    Obj2.CalculateCircumference()
    Obj2.Display()


if __name__ == "__main__":
    main()
