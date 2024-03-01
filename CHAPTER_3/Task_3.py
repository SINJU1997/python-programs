#Using arbitory argument print the students names of your class

def show(*name):
    for i in range(0,len(name)):
        print(name[i])

show("sinju","anju","divya")
