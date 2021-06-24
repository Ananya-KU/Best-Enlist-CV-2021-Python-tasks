# Create a real time scenario for inheritance example Banking concept
class bank_Account:
    def __init__(self):
        self.balance=400
        print("Welcome to Canara Bank")
    def display(self):
        print("\n Net Available Balance=",self.balance)

#Inheritance
class Deposit(bank_Account):
    def deposit(self):
        amount = int(input("Enter the amount you want to deposite: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)

#Multiple Inheritance
class withdraw(bank_Account):
    def withdraw(self):
        amount = int(input("Enter the amount you want to withdraw: "))
        if (self.balance <= amount):
            self.balance -= amount
            print("\n withdraw amount:", amount)
        else:
            print("\n Insufficient balance  ")

a= bank_Account()

p=Deposit()
p.deposit()

q=withdraw()
q.withdraw()
q.display()