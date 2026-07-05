def maximumNumber(elements):
    return max(elements)

def main():
    nNumber = int(input("Enter number of elements: "))
    numbers = []

    for i in range(nNumber):
        number = int(input("Enter a number: "))
        numbers.append(number)

    result = maximumNumber(numbers)

    print("Maximum of numbers in list is: ", result)

    ## using for
    max = 0
    
    for element in numbers:
        if element > max:
            max = element
    print("Maximum of numbers in list is: ", max)

if __name__ == "__main__":
    main()