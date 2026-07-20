def main():
    fileName = input("Enter a file name with extension to count the lines: ")
    try:
        fObj = open(fileName, "r")
        count = 0
        
        for line in fObj:
            count = count + 1
        
        print(f"Total number of lines in {fileName} are {count}")

        #lines = len(fObj.readlines())
        #print(f"Total number of lines in {fileName} are {lines}")

        fObj.close()

    except FileNotFoundError as fError:
        print("File does not exist ", fError)


if __name__ == "__main__":
    main()