from functools import reduce

multi = lambda num1, num2 : num1 * num2

def productOfNumbers(numbers):
    return reduce(multi, numbers)

def main():
    numbers = [1,2,3,4,5]
    productofAllNumber = productOfNumbers(numbers)
    print("Multiplication of numbers is: ", productofAllNumber)

if __name__ == "__main__":
    main()