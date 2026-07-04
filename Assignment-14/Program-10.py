largestNum = lambda *num, : max(num)

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    num3 = int(input("Enter third number: "))


    largest = largestNum(num1, num2, num3)
    print("Largest number is: ", largest)

if __name__ == "__main__":
    main()