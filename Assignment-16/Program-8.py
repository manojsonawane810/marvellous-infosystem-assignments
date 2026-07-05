def displayStar(num):
    for i in range(num):
        print("*")

def main():
    num = int(input("Enter a number: "))
    displayStar(num)

if __name__ == "__main__":
    main()