#Print multiplication table of given number

num=int(input("Enter a number"))
for i in range(1,11):
    print("%d * %d = %d" %(i,num,(i*num)))
