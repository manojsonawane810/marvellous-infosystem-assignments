from functools import reduce

addition = lambda num1, num2 : num1 + num2

def additionOfNumbers(numbers):
    return reduce(addition, numbers)

def main():
    numbers = [10,20,30,40,50]
    additionofAllNumber = additionOfNumbers(numbers)
    print("Addition of numbers is: ", additionofAllNumber)

if __name__ == "__main__":
    main()