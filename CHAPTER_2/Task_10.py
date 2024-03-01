#Using for loop print characters of hello world and skip the word "w"

word="Hello world"
for i in range(0,len(word)):
    if word[i] != "w":
        print(word[i])
