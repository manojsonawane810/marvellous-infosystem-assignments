from functools import reduce

filtered = lambda num : 70 <= num <= 90

mapped = lambda num : num + 10

reduced = lambda num1, num2 : num1 * num2

def filterElements(elements):
    elements = list(filter(filtered, elements))
    return elements

def mapElements(elements):
    elements = list(map(mapped, elements))
    return elements

def productOfElements(elements):
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

    elements = filterElements(elementsList)
    print("Filtered list is: ", elements)

    elements = mapElements(elements)
    print("Mapped list is: ", elements)

    product = productOfElements(elements)

    print("Product of elements is : ", product)

if __name__ == "__main__":
    main()