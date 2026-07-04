multiply = lambda num1, num2, : num1 * num2

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    multi = multiply(num1, num2)
    print("Multiplication is: ", multi)

if __name__ == "__main__":
    main()