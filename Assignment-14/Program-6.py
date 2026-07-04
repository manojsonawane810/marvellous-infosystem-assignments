checkOdd = lambda num : num % 2 != 0

def main():
    num = int(input("Enter a number: "))
    ret = checkOdd(num)

    if ret == True:
        print(num ," is odd number: ")
    else:
        print(num ," is even number")


if __name__ == "__main__":
    main()