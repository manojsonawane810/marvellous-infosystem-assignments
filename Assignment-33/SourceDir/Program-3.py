import schedule
import time
import os

def displayContent(filename):
    print("Staring file reading task...")
    border = "-"*40

    print(border + "\n")

    if os.path.exists(filename) == True:
        try:
            fObj = open(filename, "r")
            fileData = fObj.read()
            print(fileData)
        except Exception as eObj:
            print("Exception occured while opening or reading file due to insufficient permissions ", eObj)                
    else:
        print("File does not exist. Please check if filename is correct or file exist in the location")
        return

    if os.path.getsize(filename) == 0:
        print("File is empty!")
        return


    print(border + "\n")

    print("File reading task completed...")

def main():
    print("Scheduling file reading job...")

    filename = "NewDemo1.txt"

    if os.path.exists(filename) == False:
        print("File does not exist, please provide correct file.")
        return

    schedule.every().minute.do(displayContent, filename)
    
    while True:
        schedule.run_pending()
        print("Main thread is sleeping")
        time.sleep(3)

if __name__ == "__main__":
    main()