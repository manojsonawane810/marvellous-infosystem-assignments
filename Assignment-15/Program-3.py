oddNumber = lambda num : num % 2 != 0

def getOddNumbers(numbers):
    return list(filter(oddNumber, numbers))

def main():
    numbers = [11, 3, 4, 6, 27, 48, 67, 87, 96, 1]
    oddNumbers = getOddNumbers(numbers)

    print("Odd numbers are: ", oddNumbers)

if __name__ == "__main__":
    main()