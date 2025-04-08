def main():
    print("\033[1;3m temperature in Fahrenheit is converted to Celsius \033[0m]")
    degrees_fahrenheit = float(input("Enter the temperature in Fahrenheit:"))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    print(f"Temperatue in Fahrenheit {degrees_fahrenheit} = {degrees_celsius}")

if __name__ == '__main__':
    main()