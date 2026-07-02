def evenNumbers(num):
    result = 1
    while num >= result:
        if result % 2 == 0:
            print(result)
        result = result + 1

def main():
    num = int(input("Enter a number: "))
    evenNumbers(num)

if __name__ == "__main__":
    main()