#create a student file, write student details in that file,

student=open("studentdetails.txt","w")
student.write("This my test file")
student.close()

#read that file
s=open('studentdetails.txt','r')
read=s.read()
print(read)
s.close()
