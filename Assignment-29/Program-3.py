import sys

# give filename as NewDemo1.txt or Demo1.txt or NewDemo.txt.

def main():
    
    
    if len(sys.argv) > 1:    
        # using command line agruments
        fileName = sys.argv[1]
        newFileName = "Demo.txt"
        try:
            fObj = open(fileName, "r")
            data = fObj.read()
            
            fObj1 = open(newFileName, "w")
            fObj1.write(data)
            
            fObj.close()
            fObj1.close()

        except FileNotFoundError as fError:
            print("File does not exist ", fError)
    else:
        print("Please provide the filename as argument")

if __name__ == "__main__":
    main()