def main():
	num: int = 7
	num = subtract_seven(num)
	print(f"this should be zero: {num}")

def subtract_seven(num):
	num = num - 7
	return num

if __name__ == '__main__':
    main()