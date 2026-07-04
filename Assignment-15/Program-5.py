from functools import reduce

maxNumber = lambda *num : max(num)

def getMaxNumber(numbers):
    return reduce(maxNumber, numbers)

def main():
    numbers = [11, 3, 4, 6, 27, 48, 67, 87, 96, 1]
    max = getMaxNumber(numbers)
    print("Maximum number is: ", max)

if __name__ == "__main__":
    main()