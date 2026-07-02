def sumOfDigits(num):
    sum = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        sum = sum + rem

    print("Sum of digits is: ", sum)


def main():
    num = int(input("Enter a number: "))
    sumOfDigits(num)
    

if __name__ == "__main__":
    main()