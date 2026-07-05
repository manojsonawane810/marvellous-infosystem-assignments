def checkNumber(num):
    if num > 0:
        print("Positive Number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative Number")

def main():
    num = int(input("Enter a number: "))
    checkNumber(num)

if __name__ == "__main__":
    main()