checkEven = lambda num : num % 2 == 0

def main():
    num = int(input("Enter a number: "))
    ret = checkEven(num)

    if ret == True:
        print(num ," is even number: ")
    else:
        print(num ," is odd number")


if __name__ == "__main__":
    main()