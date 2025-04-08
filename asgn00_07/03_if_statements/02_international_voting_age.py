peturksbouipo_age : int = 16
stanlau_age : int = 25
mayengua_age : int = 48

def main():
    # Get the user's age
    user_age = int(input("How old are you? "))

    # Check if the user can vote in Peturksbouipo
    if user_age >= peturksbouipo_age:
        print(f"You can vote in Peturksbouipo where the voting age is {peturksbouipo_age}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {peturksbouipo_age}.")
    
    if user_age >= stanlau_age:
            print(f"You can vote in Stanlau where the voting age is {stanlau_age}.")
    else:
            print(f"You cannot vote in Stanlau where the voting age is {stanlau_age}.")

    if user_age >= mayengua_age:
            print(f"You can vote in Mayengua where the voting age is {mayengua_age}.")
    else:
            print(f"You cannot vote in Mayengua where the voting age is {mayengua_age}.")

if __name__ == '__main__':
    main()