def main():
    curr_value = int(input("Enter a number to double its value: "))  
    
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the value
        print(curr_value, end=" ") 

if __name__ == '__main__':
    main()