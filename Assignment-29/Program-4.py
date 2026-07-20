import sys
import os

# give filename as NewDemo1.txt and NewDemo.txt.

def main():
    if len(sys.argv) == 3:

        firstFileName = sys.argv[1]
        secondFileName = sys.argv[2]
        if os.path.exists(firstFileName) and os.path.exists(secondFileName):

            try:
                firstFile = open(firstFileName, "r")
                data1 = firstFile.read()

                secondFile = open(secondFileName, "r")
                data2 = secondFile.read()
                
                if data1 == data2:
                    print("Success")
                else:
                    print("Failure")
                
                firstFile.close()
                secondFile.close()
                
            except FileNotFoundError as fError:
                print("File does not exist ", fError)
        else:
            print("Files are not present. Please verify both files exists")
    else:
        print("Invalid number of aurguments")


if __name__ == "__main__":
    main()