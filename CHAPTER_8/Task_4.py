#Create a Withdrawal() method  which manages withdrawals actions.

class BankAccount:
    def __init__(self,acntnum,cname,balance):
        self.acntnum=acntnum
        self.cname=cname
        self.balance=balance

bank=BankAccount(145616598468,"SINJU SHERLY RAJU",10200)
withdraw=float(input("enter amount:"))
bank.balance=bank.balance-withdraw
print("Bank Account Details")
print("Acount number:",bank.acntnum)
print("Account Holder Name:",bank.cname)
print("Withdraw Amount:",withdraw) 
print("Cuurent Balance:",bank.balance)
