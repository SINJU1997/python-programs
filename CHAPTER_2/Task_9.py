#Using for loop print characters of welcome.If value of i=c stop the program

word="welcome"
for i in range(0,len(word)):
    if word[i]=="c":
        break
    else:
        print(word[i])
    
