def minimumNumber(elements):
    return min(elements)

def main():
    nNumber = int(input("Enter number of elements: "))
    numbers = []

    for i in range(nNumber):
        number = int(input("Enter a number: "))
        numbers.append(number)

    result = minimumNumber(numbers)

    print("Minimum of numbers in list is: ", result)

if __name__ == "__main__":
    main()