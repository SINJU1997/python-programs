#Write a program in Python to filter odd and even number from a list

a=[5,56,8,7,6,9,1,3,44,88]
evennum=[]
oddnum=[]
for i in range(0,len(a)):
    if a[i]%2 == 0:
        evennum.append(a[i])      
    else:
        oddnum.append(a[i])
        
print("Even numbers are : %s" % evennum)
print("Odd numbers are : %s" % oddnum)
