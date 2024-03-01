#create different types of inheritance (single,multiple,multi level)

#multiple inheritance

class A:
    def message1(self):
        print("Hello all, welcome to my class")

class B:
    def message2(self):
        print("Good morning all")

class c(A,B):
    def message3(self):
        print("Good afternoon all")

messages=c()
messages.message1()
messages.message2()
messages.message3()
