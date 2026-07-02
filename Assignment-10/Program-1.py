def tableOfNumber(num):
    for i in range(1, 11):
        print(num * i)

def main():
    num= int(input("Enter one number: "))
    tableOfNumber(num)

if __name__ == "__main__":
    main() 