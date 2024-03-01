#Create a display() method to display account details.


class BankAccount:
    def display(self,acntnum,cname,balance):
        print("Bank Account Details")
        print("Account number:",acntnum)
        print("Account Holder Name",cname)
        print("Account Balance",balance)

bank=BankAccount()
bank.display(16454685476,"SINJU SHERLY RAJU",20150)
