def main():
    
    print("This program allows you to sum two number")
    num1 = input("Enter First number:")
    num1 = int(num1)
    num2 = input("Enter Second number:")
    num2 = int(num2)
    totalsum = num1 + num2
    print(f"The sum of two number is {totalsum}")

# Python file to call the main() function.
if __name__ == '__main__':
    main()