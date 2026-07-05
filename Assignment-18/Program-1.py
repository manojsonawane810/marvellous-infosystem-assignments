def additionOfElements(elements):
    sum = 0
    for element in elements:
        sum = sum + element
    return sum

def main():
    nNumber = int(input("Enter number of elements: "))
    numbers = []

    for i in range(nNumber):
        number = int(input("Enter a number: "))
        numbers.append(number)

    result = additionOfElements(numbers)
    print("Addition of numbers in list is: ", result)

    ## using index
    sum = 0
    for i in range(len(numbers)):
        sum = sum + numbers[i]

    print("Addition of numbers in list using index is: ", sum)

if __name__ == "__main__":
    main()