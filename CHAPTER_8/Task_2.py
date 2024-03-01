#Create a constructor with parameters: accountNumber, name, balance.

class BankAccount:
    def __init__(self,acntnum,cname,balance):
        self.acntnum=acntnum
        self.cname=cname
        self.balance=balance

bank=BankAccount(1544659874698,"SINJU SHERLY RAJU",102530)
print("Bank Account Details")
print("Account Number:",bank.acntnum)
print("Account Holder Name:",bank.cname)
print("Account Balance:",bank.balance)

