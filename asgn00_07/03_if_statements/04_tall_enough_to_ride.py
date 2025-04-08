minimun_height : int = 50 # arbitrary units :)

def main():
    height = float(input("\033[1m;3m How tall are you? \033[0m"))
    if height >= minimun_height:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()