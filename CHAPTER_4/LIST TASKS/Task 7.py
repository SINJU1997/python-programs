#Python program to square each element of a list.

a=[2,6,4,5,8]
squre_a=[]
for i in range(0,len(a)):
    squre_a.append(a[i]**2)

print(squre_a)
