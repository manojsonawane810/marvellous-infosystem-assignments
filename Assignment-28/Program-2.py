def main():
    fileName = input("Enter a file name with extension to count the words: ")
    try:
        fObj = open(fileName, "r")
        
        count = 0
        
        for line in fObj:    
           words = line.split(" ")
           count = count + len(words)
        
        print(f"Total number of words in {fileName} are {count}")

        #lines = fObj.readlines()
        #wCount = 0
        #for line in lines:
        #    words = line.split(" ")
        #    wCount = wCount + len(words)

        #print(f"Total number of words in {fileName} are {wCount}")
        
        fObj.close()

    except FileNotFoundError as fError:
        print("File does not exist ", fError)


if __name__ == "__main__":
    main()