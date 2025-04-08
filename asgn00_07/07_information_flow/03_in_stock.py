# Define the num_in_stock function
def num_in_stock(fruit):
    # Sophia's inventory (can be customized or expanded)
    inventory = {
        'apple': 50,
        'banana': 30,
        'pear': 1000,
        'orange': 200,
        'grape': 0
    }
    
    # Return the number of the fruit in stock, or 0 if not found
    return inventory.get(fruit.lower(), 0)

# The .strip() method in Python is used to remove any leading and trailing whitespace characters
#  (such as spaces, tabs, or newlines) from a string.

# How it works:
# Leading whitespace: Whitespace characters at the beginning of the string.
# Trailing whitespace: Whitespace characters at the end of the string.
# The .strip() method returns a new string with these characters removed, without modifying the original string.

# Main function
def main():
    # Prompt the user to enter a fruit
    fruit = input("Enter a fruit: ").strip()
    
    # Get the number of the fruit in stock
    stock = num_in_stock(fruit)
    
    # Print appropriate message based on the stock count
    if stock > 0:
        print(f"This fruit is in stock! Here is how many:\n{stock}")
    else:
        print("This fruit is not in stock.")

# Call the main function to run the program
if __name__ == "__main__":
    main()
