import random

name=input("enter your name:\n")
print(f"\nWelcome! {name}")

categorey=input("\nenter your category (animals,birds,fruits,flowers)\n").lower()
if categorey=="animals":
    words=["lion","tiger","giraffe","deer","elephant","cheetah","lepoard",
       "bear","donkey","monkey","panda","buffalo","wolf","camel","horse",
       "zebra","kangaroo"]
elif categorey=="birds":
    words=["sparrow","pegion","duck","crow","robin","swan","seagull","ostrich",
           "emu","kiwi","eagle","owl","parrot","hawk","penguin"]
elif categorey=="fruits":
    words=["apple","mango","banana","kiwi","strawberry","blueberry","watermelon",
           "pineapple","papaya","mango","cherry","chikoo","orange","grapes","lychee"]
elif categorey=="flowers":
    words=["rose","lily","tulip","lotus","sunflower","jasmine","daisy","lavender","marigold","waterlily"]

word=random.choice(words)

print("\nguess the word")
guesses=""
turns=12

while turns>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_",end=" ")
            failed+=1
    if failed==0:
        print("\nCongrats!! You win......")
        print("\nThe word was: ",word)
        break

    guess=input("\nenter the letter:\n").lower()
    if len(guess)!=1:
        print("enter single letter")
        continue

    if guess in guesses:
        print("\nYou have already guessed this letter")
        continue
    guesses+=guess

    if guess not in word:
        turns-=1
        print(f"\nYou have {turns} left")

    if turns==0:
        print("\n You Lost!!")
        print("\nThe word was: ",word)


    

    
