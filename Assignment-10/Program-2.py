def sumOfNatureNumbers(num):
    sumOfNumbers = 0
    for i in range(1, num + 1):
        sumOfNumbers = sumOfNumbers + i
        
    print("Sum of first ", num , " natural numbers is : " , sumOfNumbers)

def main():
    num = int(input("Enter a number: "))
    sumOfNatureNumbers(num)

if __name__ == "__main__":
    main()