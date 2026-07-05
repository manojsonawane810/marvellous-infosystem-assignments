def displayPattern(num):
    for i in range(1, num+1):
        print("\n")
        for j in range(1, num+1):
            if i >= j:
                print(j, end="\t")


def main():
    num = int(input("Enter a number: "))
    displayPattern(num)

if __name__ == "__main__":
    main()
