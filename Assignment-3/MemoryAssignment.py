from sys import getsizeof

def getSomeInputFromUser():
    num = int(input("Enter any interger number:"))
    fNum = float(input("Enter any float number:"))
    flag = bool(input("Enter truth value:"))
    name = input("Enter your name:")    
    
    return num, fNum, flag, name

def printDataTypeOfInput(userInput):
    print("Data type of no is : ", type(userInput))

def printMemoryIdOfInput(userInput):
    print("Memory address of no is : ", id(userInput))

def printMemorySizeOfInput(userInput):
    print("Size of no is : ", getsizeof(userInput))

def main():
    userInput = getSomeInputFromUser()

    for input in userInput:
        print("Input value is: ", input)
        printDataTypeOfInput(input)
        printMemoryIdOfInput(input)
        printMemorySizeOfInput(input)

if __name__ == "__main__":
    main()