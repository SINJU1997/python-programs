#Create one class student_kit Initialize the class by taking name of the student ( constructor ).
#Display welcome message once any object is created.

class Student:
    def __init__(self,sname,course,place):
        self.sname=sname
        self.course=course
        self.place=place

#student_kit=Student()

def display():
    print("Student Name:",student_kit.sname)
    print("Course:",student_kit.course)
    print("Place:",student_kit.place)
    print("Welcome to our Institute ",student_kit.sname)
    print("\n")

num=int(input("Enter the number of students:"))

for i in range(0,num):
    name=input("Enter student name:")
    course=input("Enter your course:")
    place=input("Enter your place:")
    print("\n")
    student_kit=Student(name,course,place)
    display()
    i=i+1
    
