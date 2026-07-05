def checkNum(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

def main():
    num = int(input("Enter a number: "))
    checkNum(num)

if __name__ == "__main__":
    main()