# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second
# and also the remainder of the division.
def main():
     # Get the numbers we want to divide
     dividend: int = int(input("\033[1;3m Please enter an integer to be divided: "))  
     divisor: int = int(input("Please enter an integer to divide by: \033[0m]"))
     quotient: int = dividend // divisor  # Divide with no remainder/decimals (integer division)
     remainder: int = dividend % divisor  # Get the remainder of the division (modulo)
     print(f"The result of this division is {quotient} with a remainder of {remainder}")
     
# Python file to call the main() function.
if __name__ == '__main__':
    main()