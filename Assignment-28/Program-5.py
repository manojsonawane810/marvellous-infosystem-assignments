def main():
    fileName = input("Enter a valid file name with extension to read and search the word: ")
    wordInFile = input("Enter a word name to search in the file: ")

    if len(wordInFile) == 0:
        print("Please enter valid world name to search")
        return

    try:
        fObj = open(fileName, "r")
        found = False;
        for line in fObj:
           splines = line.split(" ")
           for spline in splines:
               if spline.replace(",", "").replace("\n","") == wordInFile:
                    print(f"{wordInFile} exists in file {fileName}")
                    found = True
                    break
            
           if found:
               break
        if found == False:
            print(f"{wordInFile} does not exist in file {fileName}")
        fObj.close()

    except FileNotFoundError as fError:
        print("File does not exist ", fError)


if __name__ == "__main__":
    main()