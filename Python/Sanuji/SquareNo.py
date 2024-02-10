def main():
    try:
        num = int(input("Enter a number: "))
        print("Squares of numbers from 1 to", num)
        for i in range(1, num + 1):
            print(i, ":", i ** 2)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
