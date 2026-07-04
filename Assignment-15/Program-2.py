evenNumber = lambda num : num % 2 == 0

def getEvenNumbers(numbers):
    return list(filter(evenNumber, numbers))

def main():
    numbers = [10, 2, 4, 5,27,49, 67, 88, 96, 0]
    evenNumbers = getEvenNumbers(numbers)

    print("Even numbers are: ", evenNumbers)

if __name__ == "__main__":
    main()