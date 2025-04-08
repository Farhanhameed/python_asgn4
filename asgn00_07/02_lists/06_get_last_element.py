def get_last_element(lst):
    """Prints the last element of a given non-empty list."""
    print(f"The Last element in the list is: {lst[-1]}")

def main():
    # Ask the user for the number of elements in the list
    while True:
        try:
            n = int(input("Enter the number of elements in the list: "))
            if n <= 0:
                print("Please enter a positive integer greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

    lst = []

    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        lst.append(element)  # Add element to the list

    # Function call to print the last element
    get_last_element(lst)

if __name__ == '__main__':
    main()
