#Create a Deposit() method which manages the deposit actions.

class BankAccount:
    def __init__(self,acntnum,cname,balance):
        self.acntnum=acntnum
        self.cname=cname
        self.balance=balance

bank=BankAccount(145616598468,"SINJU SHERLY RAJU",10200)
deposit=float(input("enter amount:"))
bank.balance=bank.balance+deposit
print("Bank Account Details")
print("Acount number:",bank.acntnum)
print("Account Holder Name:",bank.cname)
print("Deposited Amount:",deposit) 
print("Cuurent Balance:",bank.balance)
        
