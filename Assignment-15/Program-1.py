squareOfNum = lambda num: num * num

def listOfSquare(numbers):
    return list(map(squareOfNum, numbers))

def main():
    numbers = [2, 5, 8, 11, 14, 17, 20]
    sqaures = listOfSquare(numbers)
    print("Sqaure of given numbers are: ", sqaures)

if __name__ == "__main__":
    main()