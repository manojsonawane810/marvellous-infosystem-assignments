def main():
    fileName = input("Enter a file name with extension to display the lines: ")
    try:
        fObj = open(fileName, "r")
        #data = fObj.read()
        #print(data)
        
        # input file name Demo.txt
        #for line in fObj:
        #    print(line)

        # input file name Demo1.txt
        lines = fObj.readlines()
        
        for line in lines:
            splitLines = line.split(".")
            for spline in splitLines:
                spline = spline.removeprefix(" ").removesuffix(" ")
                print(spline)

        fObj.close()

    except FileNotFoundError as fError:
        print("File does not exist ", fError)


if __name__ == "__main__":
    main()