#Accept different data type from users and display the type of data and types of data
name=input("Enter your name")
age=int(input("Enter your age"))
mark=float(input("Enter your mark"))
nametype=type(name)
agetype=type(age)
marktype=type(mark)
print("My name is %s and I'm %d years old. My mark is %f" %(name,age,mark))
print("%s is %s" %(name,nametype))
print("%d is %s" %(age,agetype))
print("%f is %s" %(mark,marktype))