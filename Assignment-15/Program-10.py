evenNumber = lambda num : num % 2 == 0


def getEvenNumberCount(numbers):
    evenNumbers = list(filter(evenNumber, numbers))
    return len(evenNumbers)

def main():
    numbers = [10, 2, 4, 5,27,49, 67, 88, 96, 0]
    evenNumberCount = getEvenNumberCount(numbers)

    print("Even numbers count it: ", evenNumberCount)

if __name__ == "__main__":
    main()