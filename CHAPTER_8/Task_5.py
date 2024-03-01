#Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.

class BankAccount:
    def __init__(self,acntnum,cname,balance):
        self.acntnum=acntnum
        self.cname=cname
        self.balance=balance

bank=BankAccount(145616598468,"SINJU SHERLY RAJU",20000)
cblanace=bank.balance
bank.balance=bank.balance-(5/100)
print("Bank Account Details")
print("Acount number:",bank.acntnum)
print("Account Holder Name:",bank.cname)
print("Balance:",cblanace) 
print("Cuurent Balance:",bank.balance)
