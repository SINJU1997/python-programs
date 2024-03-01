#Create a list and print elements using iter and next

numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
print("My list is",numbers)
for i in numbers:
    print(next(iterator))
