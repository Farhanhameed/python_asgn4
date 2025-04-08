affirmation : str = "I am capable of doing anything I put my mind to."

def main():
    print(f"Please type the following affirmation: {affirmation}")

    user_feedback = input()  # Get user's input
    while user_feedback != affirmation:  # While the user's input isn't the affirmation
        # Tell the user that they did not type the affirmation correctly
        print("That was not the affirmation.")

        # Ask the user to type the affirmation again!
        print(f"Please type the following affirmation: {affirmation}")
        user_feedback = input()

    print("That's right! :)")

if __name__ == '__main__':
    main()