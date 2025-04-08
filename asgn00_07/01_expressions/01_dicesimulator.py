"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times.  Prints
the results of each die roll.  This program is used
to show how variable scope works.
"""

# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
num_side = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1 = random.randint(1, num_side)
    die2 = random.randint(1, num_side)
    total = die1 + die2
    print(f"Total of two dice is: {total}")

def main():
    die1: int = 10
    print(f"die1 in main() starts as: {die1}")
    roll_dice()
    roll_dice()
    roll_dice()
    print(f"die1 in main() starts as: {die1}")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()