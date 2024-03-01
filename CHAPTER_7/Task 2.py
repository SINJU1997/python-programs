#user enter a negative number raise exception

number=int(input("enter a number"))
if number<0:
    raise Exception("Number is NEGATIVE")
else:
    print(number)


