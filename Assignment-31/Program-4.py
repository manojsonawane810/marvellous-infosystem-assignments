import schedule
import os
import datetime
import time

def logFileGeneration():
    print("Log generation started")
    filename = logFileNameCreation()

    if os.path.exists(filename) == False:
        fObj = open(filename, "w")
    else:
        fObj = open(filename, "a")

    datetimeVal = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    fObj.write("Log file created successfully." + "\n")
    fObj.write("Creation time: " + datetimeVal)

    fObj.close()
    print("Log generation completed")


def formattedDatTimeString(dateTimeVal):
    dateTimeVal = dateTimeVal.replace(" ", "_")
    dateTimeVal = dateTimeVal.replace(":", "_")
    dateTimeVal = dateTimeVal.replace("-", "_")
    return dateTimeVal

def logFileNameCreation():
    logFileName = "MarvellousLog.txt"

    datateTimeVal = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    datateTimeVal = formattedDatTimeString(datateTimeVal)

    filename, fileextension = os.path.splitext(logFileName)
    filename = filename + "_"+ datateTimeVal + fileextension

    return filename


def main():
    print("Scheduling log file creation job...")
    
    schedule.every(5).seconds.do(logFileGeneration)

    while True:
        schedule.run_pending()
        print("Main thread is sleeping")
        time.sleep(3)

if __name__ == "__main__":
    main()