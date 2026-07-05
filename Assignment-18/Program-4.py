def searchNumberFrequency(searchNum, numbers):
    count = 0
    for no in numbers:
        if no == searchNum:
            count = count + 1
    return count


def main():
    nNumber = int(input("Enter number of elements: "))
    numbers = []

    for i in range(nNumber):
        number = int(input("Enter a number: "))
        numbers.append(number)

    print("Input elements are: ", numbers)

    searchNum = int(input("Enter number to search in list: "))

    result = searchNumberFrequency(searchNum, numbers)

    print(f"Frequency of number {searchNum} in list is: {result}")

if __name__ == "__main__":
    main()