#Create a tuple and perform add,delete,change elements(conver it in list)

#add item
colors=("red","orange","black","blue")
newcolor= ("yellow",)
colors += newcolor
print(colors)

#remove item
colors=("red","orange","black","blue")
y=list(colors)
y.remove("black")
colors=tuple(y)
print(colors)

#change particular item
colors=("red","orange","black","blue")
y = list(colors)
y[1] = "pink"
colors = tuple(y)
print(colors)
