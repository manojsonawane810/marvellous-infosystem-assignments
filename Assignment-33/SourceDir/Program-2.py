import schedule
import time
import os
import datetime

def monitorFile(filename):
    print("Staring file moniroing task...")
    border = "-"*40
    if os.path.exists(filename):

        filepath = os.path.realpath(filename)
        fileSize = os.path.getsize(filename)
        datetimeVal = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

        logFile = "FileSizeLog.txt"

        if os.path.exists(logFile) == False:
            fObj = open(logFile, "w")
        else:
            fObj = open(logFile, "a")

        fObj.write(border + "\n")
        fObj.write("File path : " + filepath + "\n")
        fObj.write(f"File size in bytes : {fileSize} \n")
        fObj.write("Date and time : " + datetimeVal + "\n")
        fObj.write(border + "\n")
    else:
        print("File does not exist. Please check if filename is correct or file exist in the location")

    print("File moniroing task completed...")

def main():
    print("Scheduling file monitoring job...")

    filename = "NewDemo1.txt"

    if os.path.exists(filename) == False:
        print("File does not exist, please provide correct file.")
        return

    
    schedule.every(30).seconds.do(monitorFile, filename)
    
    while True:
        schedule.run_pending()
        print("Main thread is sleeping")
        time.sleep(20)

if __name__ == "__main__":
    main()