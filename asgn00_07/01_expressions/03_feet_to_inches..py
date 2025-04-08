# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.
inches_in_foot: int = 12 # Conversion factor. There are 12 inches for 1 foot.

def main():
    feet:float = float(input("Enter number of feet: ")) # Get the number of feet
    inches: float = feet * inches_in_foot # Perform the conversion
    print(f"That is {inches} inches!")

if __name__ == '__main__':
    main()