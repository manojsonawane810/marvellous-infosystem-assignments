maxNumber = lambda num1, num2 : max(num1, num2)

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    max = maxNumber(num1, num2)
    print("Max number is: ", max)

if __name__ == "__main__":
    main()