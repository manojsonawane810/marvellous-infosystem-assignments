cubeOfNumber = lambda num : num * num * num

def main():
    num = int(input("Enter a number to calculate cube of number: "))
    ret = cubeOfNumber(num)
    print("Cube of the number ", num ," is ", ret)

if __name__ == "__main__":
    main()