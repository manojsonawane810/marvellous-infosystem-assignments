def addition(*num):
    sum = 0
    for no in num:
        sum = sum + no
    return sum

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter secodn number: "))

    add = addition(num1, num2)
    print("Addition of numbers is: ", add)

if __name__ == "__main__":
    main()