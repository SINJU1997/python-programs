#create a basic calculator using magical methods(operator overloading)

num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

print(num1,"+",num2,"=",((num1).__add__(num2)))
print(num1,"-",num2,"=",((num1).__sub__(num2)))
print(num1,"*",num2,"=",((num1).__mul__(num2)))
print(num1,"/",num2,"=",((num1).__divmod__(num2)))
