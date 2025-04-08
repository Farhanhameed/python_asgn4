def main():
    # Ask the user for their favorite animal
    favorite_animal = input("\033[1;3m What's your favorite animal? \033[0m")

    # Respond with the same animal
    print(f"My favorite animal is also {favorite_animal}!")

if __name__ == '__main__':
    main()