# Simulate rolling two dice, and prints results of each roll as well as the total.

# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
num_sides: int = 6

def main():   
    # Roll die
    die1: int = random.randint(1, num_sides)
    die2: int = random.randint(1, num_sides)
    
    # Get their total
    total: int = die1 + die2
    
    # Print out the results
    print("Dice have", num_sides, "sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

# to call the main() function.
if __name__ == '__main__':
    main()