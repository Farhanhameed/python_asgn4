import random

print("=== Welcone to password generator ===")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),./';][]1234567890"

number = int(input("Enter the number of password: "))

length = int(input("the lenght of password required: "))

print("\n Here are password as you required")

for pwd in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)