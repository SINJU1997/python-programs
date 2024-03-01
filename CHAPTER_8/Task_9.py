#Write a python program for method overloading

class Person:
    def display(self,message=None):
        if message is not None:
            print(message)
        else:
            print("No message")

persons=Person()
persons.display()
persons.display("Welcome")
