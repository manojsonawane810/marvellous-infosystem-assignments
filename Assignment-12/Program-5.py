def printAllNumbers(num):
    for no in range(num, 0, -1):
        print(no)

def main():
    num = int(input("Enter a number: "))

    printAllNumbers(num)

if __name__ == "__main__":
    main()