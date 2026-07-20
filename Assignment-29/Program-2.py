import sys

# give filename as NewDemo1.txt or Demo1.txt or NewDemo.txt
def main():
    
    
    if len(sys.argv) > 1:    
        # using command line agruments
        fileName = sys.argv[1]
        
        # using user input
        #fileName = input("Enter a file name with extension to display the lines: ")
        try:
            fObj = open(fileName, "r")
            data = fObj.read()
            #data = fObj.readlines()
            
            print(data)
            
            fObj.close()

        except FileNotFoundError as fError:
            print("File does not exist ", fError)
    else:
        print("Please provide the filename as argument")

if __name__ == "__main__":
    main()