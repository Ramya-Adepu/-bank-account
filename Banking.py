class Account:
    def __init__(self, name):
        self.name=name
        self.balance=0

    def withdrawl(self, amount):
        if(amount>self.balance):
            print("Withdrawl notpoosible due to lack of sufficient funds")
        elif(amount<0):
            print("Please ener valid amount for withdrawl")
        else:
            c=self.balance-amount
            self.balance=c
            print(f"The balance after withdrawl is {self.balance}")

    def deposit(self, amount):
        if(amount<0):
            print("Please deposit valid amount")
        else:
            d=self.balance+amount
            self.balance=d
            print(f'The balance after deposit is   {self.balance}')


Account=Account("Ramya")
Account.withdrawl(40)
Account.deposit(10000)
Account.deposit(20_000)
Account.withdrawl(6908)
Account.deposit(30_00)
Account.withdrawl(300000)
        

