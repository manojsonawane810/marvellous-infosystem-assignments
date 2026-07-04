minNumber = lambda num1, num2 : min(num1, num2)

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    min = minNumber(num1, num2)
    print("Min number is: ", min)

if __name__ == "__main__":
    main()