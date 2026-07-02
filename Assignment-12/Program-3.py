def calculate(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2

    print("Addition is: ", addition)
    print("Subtraction is: ", subtraction)
    print("Multiplication is: ", multiplication)
    print("Division is : ", division)
    

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    calculate(num1, num2)


if __name__ == "__main__":
    main()