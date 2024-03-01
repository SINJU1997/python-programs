#Accept two numbers from the user and display their sum, multiplication and division.
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
addition=num1+num2
subtraction=num1-num2
multiplication=num1*num2
division=num1/num2
print("Result is")
print("%d + %d = %d" %(num1,num2,addition))
print("%d - %d = %d" %(num1,num2,subtraction))
print("%d * %d = %d" %(num1,num2,multiplication))
print("%d / %d = %f" %(num1,num2,division))
