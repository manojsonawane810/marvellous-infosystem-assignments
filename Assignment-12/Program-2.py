def printFactors(num):
    evenNum = num % 2 == 0
    halfNum = num // 2
    for no in range(1, halfNum + 1):
        if num % no == 0:
            print(no)
    print(num)

def main():
    num = int(input("Enter a number: "))
    printFactors(num)

if __name__ == "__main__":
    main()