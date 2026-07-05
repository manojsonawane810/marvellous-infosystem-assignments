def displayPattern(num):
    for i in range(num):
        if i != 0:
            print("\n")
        for j in range(num):
            print("*", end="\t")

def main():
    num = int(input("Enter a number: "))
    displayPattern(num)

if __name__ == "__main__":
    main()