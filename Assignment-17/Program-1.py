from Arithmetic import add, sub, multi, div

def calculate(num1, num2):
    addition = add(num1, num2)
    substraction = sub(num1, num2)
    multiplication = multi(num1, num2)
    division = div(num1, num2)

    return addition, substraction, multiplication, division

def main():
    print("-"*40)
    print("Arithmetic calculation program")
    print("-"*40)
    print()
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    add, sub, multi, div = calculate(num1, num2)
    
    print("Addition is: ", add)
    print("Substraction is: ", sub)
    print("Multiplication is: ", multi)
    print("Division is: ", div)

if __name__ == "__main__":
    main()