squareOfNumber = lambda num: num * num;

def main():
    num = int(input("Enter a number to calculate square of number: "))
    ret = squareOfNumber(num)
    print("Square of the number ", num ," is ", ret)

if __name__ == "__main__":
    main()