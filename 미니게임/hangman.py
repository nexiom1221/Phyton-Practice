from random import *

words = ['apple','banana','orange','melon','watermelon','mango','strawberry']
word = choice(words)

print("answer : " + word)

letters = ""

count = 0

while True:
    succeed = True
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()

    if succeed:
        print("Success")
        break

    letter = input("Input letter > ")
    if letter not in letters:
        letters += letter
    
    if letter in word:
        print("Correct")
    else:
        print("Wrong")
        count += 1
    
    if count ==7:
        print("Fail")
        break
    

