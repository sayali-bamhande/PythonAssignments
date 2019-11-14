class Numbers:

    Value = None

    def __init__(self, no):
        Numbers.Value = no

    def ChkPrime(self):
        flag = True
        for i in range(2, int(self.Value / 2) + 1):
            if Numbers.Value % i == 0:
                flag = False
                break
        return flag

    def Factors(self):
        factors = list()
        for i in range(1, int(self.Value / 2) + 1):
            if Numbers.Value % i == 0:
                factors.append(i)

        return factors

    def SumFactors(self):
        sum = 0
        for i in range(1, int(self.Value / 2) + 1):
            if Numbers.Value % i == 0:
                sum += i
        return sum

    def ChkPerfect(self):
        if self.SumFactors() == Numbers.Value:
            return True
        else:
            return False


def main():
    n = int(input("Enter the Number :"))
    ob1 = Numbers(n)
    print("Is Prime :", ob1.ChkPrime())
    print("Is Perfect :", ob1.ChkPerfect())
    print("Its Factors :", ob1.Factors())
    print("Its sum of factors :", ob1.SumFactors())




if __name__ == "__main__":
    main()
