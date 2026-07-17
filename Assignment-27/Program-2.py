class BankAccount:
    ROI = 10.5

    def __init__(self, accHolderName, amount):
        self.name = accHolderName
        self.amount = amount

    def display(self):
        print("\n")
        print(f"Account holder name is: {self.name} and current balance is: {self.amount}")

    def deposit(self):
        print("\n")
        print("Enter the amount to deposit in your account:")
        dAmount = int(input())

        if dAmount > 0:
            self.amount = self.amount + dAmount
            self.display()
        else:
            print("Enter valid positive amount to deposit")
            self.deposit()
        
    
    def withdraw(self):
        print("\n")
        print("Enter the amount to withdraw from your account:")
        wAmount = int(input())

        if wAmount > 0:
            if self.amount > 0 and self.amount >= wAmount:
                self.amount = self.amount - wAmount
                self.display()
            else:
                print("Insufficient balance")
        else:
            print("Enter valid positive amount to withdraw")
            self.withdraw()
    
    def calculateInterest(self):
        iAmount = (self.amount * BankAccount.ROI) / 100
        print(f"Interest gained is: {iAmount:.2f}")


    print("-"*40)
    print("Welcome to Banking System")
    print("-"*40)


bObj1 = BankAccount("Dinesh", 35000.00)

bObj1.display()
bObj1.deposit()
bObj1.withdraw()
bObj1.deposit()
bObj1.calculateInterest()


bObj2 = BankAccount("Rahul", 145890.60)

bObj2.display()
bObj2.deposit()
bObj2.withdraw()
bObj2.deposit()
bObj2.calculateInterest()