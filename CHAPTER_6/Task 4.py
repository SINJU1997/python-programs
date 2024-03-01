#Create a employee file and save input data that file.read it

emp=open("employee.txt","w")
name=input("enter employee name \n")
designation=input("enter designation \n")
emp.write("Name : %s \n" %name)
emp.write("Designation : %s" %designation)
emp.close()

e=open("employee.txt","r")
print(e.read())
e.close()
