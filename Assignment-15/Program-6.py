from functools import reduce

minNumber = lambda *num : min(num)

def getMinNumber(numbers):
    return reduce(minNumber, numbers)

def main():
    numbers = [11, 3, 4, 6, 27, 48, 67, 87, 96, 1]
    min = getMinNumber(numbers)
    print("Minimum number is: ", min)

if __name__ == "__main__":
    main()