class BankAccount:
    ROI = 10.5

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def Display(self):
        print("Name : ", self.name)
        print("Your current balance : ", self.amount)

    def Deposit(self, credit):
        if credit > 0:
            self.amount = self.amount + credit
        else:
            print("Invalid amount...")
        print("Balance is : ",self.amount)

    def Withdraw(self, debit):
        if self.amount >debit:
            self.amount = self.amount - debit
        else:
            print("You don't have sufficient balance...")
        self.Display()
        print("Balance is : ",self.amount)

    def CalculateInterest(self):
        interest = (self.amount * BankAccount.ROI)/100
        print("Interest calculated on your amount is : ", interest)


def main():
    name = input("Enter the account holder name :")
    amount = float(input("Enter the current balance of account :"))
    Obj1 = BankAccount(name, amount)
    Obj1.Display()
    dt = float(input("Enter amount to credit to account : "))
    Obj1.Deposit(dt)
    dt = float(input("Enter amount to debit from account : "))
    Obj1.Withdraw(dt)
    Obj1.CalculateInterest()


if __name__ == "__main__":
    main()
