#Find simple Interest from user input data
p=int(input("Enter initial principal balance"))
r=int(input("Enter annual inetrest rate"))/100
t=int(input("Enter time"))
A=p*(1+r*t)
print("Your simple interest is %f" %A)
