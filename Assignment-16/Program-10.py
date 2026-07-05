def calculateLength(name):
    length = len(name)
    print("Length of given name is: ", length)

def main():
    name = input("Enter any name: ")
    calculateLength(name)

if __name__ == "__main__":
    main()