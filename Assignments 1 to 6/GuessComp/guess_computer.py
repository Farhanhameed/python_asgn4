import random

def guess(x):
    random_numbers = random.randint(1, x)
    guess = 0
    while guess != random_numbers:
        guess = int(input("Guess a number from 1 to {x}: "))
        if guess < random_numbers:
            print("Sorry, guess again, Too low.")
        elif guess > random_numbers:
            print("Sorry, guess again, Too high.")
    print(f"Congrats, You have guessed the number {x}")

guess(10)    