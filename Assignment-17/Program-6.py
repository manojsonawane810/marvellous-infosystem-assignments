def displayPattern(num):
    for i in range(num):
        print("\n")
        for j in range(num):
            if j + i < num:
                print("*", end="\t")

def displayPatternUsingWhile(num):
    for i in range(num):
        print("\n")
        
        j = i
        while j < num:
            print("*", end="\t")
            j = j + 1


def main():
    num = int(input("Enter a number: "))
    displayPattern(num)
    displayPatternUsingWhile(num)

if __name__ == "__main__":
    main()
