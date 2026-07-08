from functools import reduce

filtered = lambda num : num % 2 == 0

mapped = lambda num : num ** 2

reduced = lambda num1, num2 : num1 + num2

def filterElements(elements):
    elements = list(filter(filtered, elements))
    return elements

def mapElements(elements):
    elements = list(map(mapped, elements))
    return elements

def additionOfElements(elements):
    return reduce(reduced , elements)

def main():
    numberOfElement = int(input("Enter number of elements in list: "))
    print("\n")
    elementsList = []
    for i in range(numberOfElement):
        print("Enter a number: ")
        number = int(input())
        elementsList.append(number)

    print("Input list is: ", elementsList)

    if len(elements) > 0:
        elements = filterElements(elementsList)
        print("Filtered list is: ", elements)

        if len(elements) > 0:
            elements = mapElements(elements)
            print("Mapped list is: ", elements)

            addition = additionOfElements(elements)
            print("Addition of elements is : ", addition)

if __name__ == "__main__":
    main()