from MarvellousNum import chkPrime


def listPrime(elements):
    sum = 0
    for element in elements:
        isPrime =  chkPrime(element)
        if isPrime == True:
            sum = sum + element
            print(f"{element} is prime number")
    return sum

def main():
    numberOfElements = int (input("Enter nunber of elements to be added in list: "))
    elements = []

    for i in range(numberOfElements):
        num = int(input("Enter a number: "))
        elements.append(num)

    result = listPrime(elements)
    print("Addition is: ", result)

if __name__ == "__main__":
    main()