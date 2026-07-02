def checkDivisibleBy(no1):
    if no1 % 3 == 0 and no1 % 5 == 0:
        print("Entered number is divisible by 3 and 5")
    else:
        print("Entered number is not divisible by 3 and 5")

def main():
    no1 = int(input("Enter number to check divisible by 3 and 5:"))
    checkDivisibleBy(no1)

if __name__ == "__main__":
    main()