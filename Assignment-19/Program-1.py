powerOfTwo = lambda num : num ** 2

def main():
    num = int(input("Enter a number: "))

    ret = powerOfTwo(num)

    print(f"Power of two of number is {ret}")

if __name__ == "__main__":
    main()