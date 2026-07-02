def oddNumbers(num):
    for no in range(1, num + 1):
        if no % 2 != 0:
            print(no)

def main():
    num = int(input("Enter a number: "))
    oddNumbers(num)

if __name__ == "__main__":
    main()