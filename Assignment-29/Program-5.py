# give filename as NewDemo1.txt or Demo1.txt or NewDemo.txt and search word day or morning or nice.
def main():
    fileName = input("Enter a valid file name with extension to read and search the word: ")
    wordInFile = input("Enter a word name to search in the file: ")

    if len(wordInFile) == 0:
        print("Please enter valid world name to search")
        return

    try:
        fObj = open(fileName, "r")
        count = 0

        for line in fObj:
           splines = line.split(" ")

           for spline in splines:
               if spline.replace(",", "").replace("\n","").replace(".","").replace("!","") == wordInFile:
                    count = count + 1
        
        print(f"Occurrences of {wordInFile} in file {fileName} is {count}")


        fObj.close()
    except FileNotFoundError as fError:
        print("File does not exist ", fError)


if __name__ == "__main__":
    main()