#solve overriding problem using super function

class A:
    def message(self):
        print("Welcome all")

class B(A):
    def message(self):
        print("Good morning")
        super().message()

obj=B()
obj.message()
        
