import random

num = random.randint(1, 100)

print("Guess the Number between 1 and 100")

count = 0

while True:
    guess = int(input("Enter your guess: "))
    count += 1

    if guess == num:
        print("You guessed the number in", count, "attempt(s)")
        break
    elif guess < num:
        print("Guess is lower than the number")
    else:
        print("Guess is higher than the number")
