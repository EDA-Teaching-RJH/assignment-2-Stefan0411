import random

print("I'm thinking about a number from 1 to 100.. Try and guess it! :D")

correct_number = random.randint(1, 100)
guess = None

while guess != correct_number:
    guess = int(input("Enter your guess:"))

    if guess < correct_number:
        print("Too low! Try again.")
    elif guess > correct_number:
        print("Too high! Try again.")
    else:
        print("Congrats! You guessed the number correctly!")