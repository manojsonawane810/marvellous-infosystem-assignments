def addittionOfDigits(num):
    sum = 0
    rem = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        sum = sum + rem
    
    return sum

def main():
    num = int(input("Enter a number: "))
    addition = addittionOfDigits(num)
    print("Addition is: ", addition)


if __name__ == "__main__":
    main()