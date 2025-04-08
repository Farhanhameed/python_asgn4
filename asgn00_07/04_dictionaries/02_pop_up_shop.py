def main():
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input(f"\033[1;3m How many {fruit_name} do you want to buy?: \033[0m"))
        total_cost += (price * amount_bought)
    
    print(f"Your total is ${total_cost}")

if __name__ == '__main__':
    main()