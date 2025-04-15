# Mars Weight Solution

# There are three key stages to solving this problem:
# Getting the Earthling's weight from them, which we need the input function for. 
# Converting the Earthing's weight from a string to a number so we can do math with it.
# We use the float function to do this, since the weight isn't necessarily a whole number
# Calculating the weight on Mars, which we do by multiplying the Earth weight by 0.378. 
# To make the program easy to read, we store this number in a constant called MARS_MULTIPLE.
# Check out the solution code to see all of these stages in action!

"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""

# We use constants!
MARS_MULTIPLE = 0.378

def main():
    earth_weight_str = input('Enter a weight on Earth: ')

    # Get the numeric value since input() returns a value in string form
    earth_weight = float(earth_weight_str)

    # Having a variable for each piece of information is a good habit
    mars_weight = earth_weight * MARS_MULTIPLE
    rounded_mars_weight = round(mars_weight, 2)

    # Note the string concatenation!
    print(f'The equivalent weight on Mars: {rounded_mars_weight}')

if __name__ == '__main__':
    main()

# Planetary Weights Solution

# There are two key parts to this solution:
# Everything from the first part of the problem: getting a user's input, converting it to a float 
# to do the calculation, and covering it to a string to print it out.
# Using if statements to check which gravitational constant to use based on the user's input.  
# Solution

"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""

def main():
        # Dictionary to store planet gravity factors
    planet_gravity = {
        "mercury": 0.376,
        "venus": 0.889,
        "mars": 0.378,
        "jupiter": 2.36,
        "saturn": 1.081,
        "uranus": 0.815,
        "neptune": 1.14
    }

    # Prompt the user for their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Prompt the user for the name of a planet
    planet = input("Enter a planet: ").lower()

 # Checking if planet is valid and calculating weight
    if planet in planet_gravity:
        planet_weight = round(earth_weight * planet_gravity[planet], 2)
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("Invalid planet name. Please enter a valid planet from the solar system.")

    # # Print the result
    # print(f"The equivalent weight on {planet} : {rounded_planetary_weight}")

if __name__ == "__main__":
    main()