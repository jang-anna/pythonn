
from random import * 
words = ["banana","pineapple","grape"] 
word = choice(words) 
letters = "" 


while True:         
    succeed = True 
    print()
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