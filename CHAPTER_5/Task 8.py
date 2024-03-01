#create a calculator package(include 4 modules +,-,*,/).

def add(a,b):
    return a+b

def subs(a,b):
    return a-b

def mul(a,b):
    return a*b

def divi(a,b):
    return a/b


print("Select the operation")
print("1. ADDITION")
print("2. SUBTRACTION")
print("3. MULTIPLICATION")
print("4. DIVISION")

while True:
    choice=input("enter your choice")

    
    if choice in ('1', '2', '3', '4'):
        try:
            num1=float(input("enter first number"))
            num2=float(input("enter second number"))
        except ValueError:
            print("Invalid input. Please enter a number")
            continue
        if choice=="1":
            ans=add(num1,num2)
            print(num1,"+",num2,"=",ans)
        elif choice=="2":
            ans=subs(num1,num2)
            print(num1,"-",num2,"=",ans)
        elif choice=="3":
            ans=mul(num1,num2)
            print(num1,"*",num2,"=",ans)
        elif choice=="4":
            ans=divi(num1,num2)
            print(num1,"/",num2,"=",ans)

            
        nextcal=input("Need next calculation(yes/no)")
        if nextcal=="no":
            break
    else:
        print("Invalid input")
    
