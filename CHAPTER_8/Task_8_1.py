#create different types of inheritance (single,multiple,multi level)

#single inheritance

class A:
    def message1(self):
        print("Hello all, welcome to my class")

class B(A):
    def message2(self):
        print("Good morning all")

messages=B()
messages.message1()
messages.message2()
