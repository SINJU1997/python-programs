#Write a program to display those items from a list that is divisible by 5.

a=[1,65,80,9,6,7]
for i in range(0,len(a)):
    if a[i]%5==0:
        print(a[i])
