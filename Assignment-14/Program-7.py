checkDivisible = lambda num : num % 5 == 0

def main():
    num = int(input("Enter a number: "))
    ret = checkDivisible(num)

    if ret == True:
        print(num ," is divisible by 5")
    else:
        print(num ," is not divisible by 5")


if __name__ == "__main__":
    main()