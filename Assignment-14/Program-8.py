addition = lambda num1, num2, : num1 + num2

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    add = addition(num1, num2)
    print("Addition is: ", add)

if __name__ == "__main__":
    main()