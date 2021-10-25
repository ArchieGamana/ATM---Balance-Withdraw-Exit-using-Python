import sys
class Customer:
    '''Customer class with bank related operation'''
    bankname="Philippine Bank" #static variable
    def __init__(self, n, bal=0.0):
        self.name = n
        self.balance = bal

    def deposite(self,amt):
        self.balance=self.balance+amt
        print("Your Current Account Balance is",self.balance)

    def withdraw(self,amt):
        if amt > self.balance:
            print("Insufficient funds can't perform withdraw... this time")
            sys.exit()
        self.balance = self.balance-amt
        print("Balance After Withdraw is", self.balance)

print("Welcome to", Customer.bankname)
name = input("Enter Customer Name: ")
c = Customer(name)

while True:
    print("Choose your Option: \n 'D' --> Deposit\n 'W' --> Withdraw\n 'E' --> Exit 'B' --> Balance ")
    option = input("Enter Your Option: ")
    if option == 'd' or option == 'D':
        print("**************** Deposit Option ****************")
        amount = float(input("Enter Deposit Amount: "))
        c.deposite(amount)
    elif option == 'w' or option == 'W':
        print("**************** Withdraw Option ****************")
        amount = float(input("Enter Withdraw Amount: "))
        c.withdraw(amount)
    elif option == 'e' or option == 'E':
        print("Thank you for banking with us...")
        sys.exit()
    else:
        print("Invalid Option")
