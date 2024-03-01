#Diplay multiples of given number in the range 1 to 100

number=int(input("Enter a number"))
for i in range(1,101):
    result= i*number
    print("%d * %d = %d" %(i,number,result))
