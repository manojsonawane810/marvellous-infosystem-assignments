from functools import reduce

def filtered(num):
    count = 0

    for i in range(1, num+1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        return True
    else:
        return False

mapped = lambda num : num * 2

def reduced(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def filterElements(elements):
    elements = list(filter(filtered, elements))
    return elements

def mapElements(elements):
    elements = list(map(mapped, elements))
    return elements

def MaximumOfElements(elements):
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

    if len(elementsList) > 0:
        elements = filterElements(elementsList)
        print("Filtered list is: ", elements)

        if len(elements) > 0:
            elements = mapElements(elements)
            print("Mapped list is: ", elements)

            max = MaximumOfElements(elements)
            print("Maximum of elements is : ", max)

if __name__ == "__main__":
    main()