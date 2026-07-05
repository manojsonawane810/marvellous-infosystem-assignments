def displayPattern(num):
    for i in range(1, num+1):
        print("\n")
        for j in range(1, num+1):        
            print(j, end="\t")

def displayPatternUsingWhile(num):
    for i in range(1, num+1):
        print("\n")
        
        j = 1
        while j  < num + 1:
            print(j, end="\t")
            j = j + 1


def main():
    num = int(input("Enter a number: "))
    displayPattern(num)
    print("\n")
    print("-"*40)
    displayPatternUsingWhile(num)

if __name__ == "__main__":
    main()
