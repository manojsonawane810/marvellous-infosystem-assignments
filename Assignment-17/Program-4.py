def additionOfFactors(num):
    sum = 0
    halfNum = num // 2 + 1

    for i in range(1, halfNum):
        if num % i == 0:
            sum = sum + i
    return sum

def main():
    num = int(input("Enter a number: "))
    addition = additionOfFactors(num)
    print(f"Addition of factors is {addition}")

if __name__ == "__main__":
    main()