divisibleBy3Or5 = lambda num: num % 3 == 0 and num % 5 == 0 

def divisibleBy(numbers):
    return list(filter(divisibleBy3Or5, numbers ))

def main():
    numbers = [15, 30, 4, 60, 27, 45, 65, 87, 96, 1]
    result = divisibleBy(numbers)
    print("Numbers divisible by 3 and 5 are: ", result)

if __name__ == "__main__":
    main()