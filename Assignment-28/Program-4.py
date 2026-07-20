def main():
    fileName = input("Enter a file name with extension to copy the lines: ")
    newFileName = input("Enter a file name with extension to write the lines: ")
    try:
        oldFile = open(fileName, "r")
        data = oldFile.read()
        
        newFile = open(newFileName, "w")
        newFile.write(data)
        newFile.close()
        oldFile.close()

        readNewFile = open(newFileName, "r")

        for line in readNewFile:
           print(line)

        readNewFile.close()
        
    except FileNotFoundError as fError:
        print("File does not exist ", fError)


if __name__ == "__main__":
    main()