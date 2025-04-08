import random

n_numbers : int = 10
min_value : int = 1
max_value : int = 100

def main():
    for i in range(n_numbers):
        value = random.randint(min_value, max_value)
        print(value, end=" ")

if __name__ == '__main__':
    main()