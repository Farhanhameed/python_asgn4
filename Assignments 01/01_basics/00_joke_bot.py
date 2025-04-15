PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY: str = "Sorry I only tell jokes."

def main():
    # Asking the user for input
    user_input = input(PROMPT)
    
    # Checking if the user input is "Joke"
    if user_input == "joke":
        print(JOKE)  # Print the joke
    else:
        print(SORRY)  # Print the sorry message


if __name__ == "__main__":
    main()