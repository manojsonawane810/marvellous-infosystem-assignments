import schedule
import os
import datetime
import time

def fileGeneration():
    border = "-"*40
    print("File generation started")
    filename = fileNameCreation()

    fObj = open(filename, "w")

    currentDate = datetime.datetime.now().strftime("%d-%m-%Y")
    currentTime = datetime.datetime.now().strftime("%I:%M:%S %p")

    fObj.write(border + "\n")
    fObj.write("Filename : " + filename + "\n")
    fObj.write("Creation date : " + currentDate + "\n")
    fObj.write("Creation time : " + currentTime + "\n")
    fObj.write(border + "\n")

    fObj.close()
    print("File generation completed")


def formattedDatTimeString(dateTimeVal):
    dateTimeVal = dateTimeVal.replace(" ", "_")
    dateTimeVal = dateTimeVal.replace(":", "_")
    dateTimeVal = dateTimeVal.replace("-", "_")
    return dateTimeVal

def fileNameCreation():
    fileName = "File.txt"

    datateTimeVal = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    datateTimeVal = formattedDatTimeString(datateTimeVal)

    filename, fileextension = os.path.splitext(fileName)
    filename = filename + "_"+ datateTimeVal + fileextension

    return filename


def main():
    print("Scheduling file creation job...")
    
    schedule.every().minute.do(fileGeneration)

    while True:
        schedule.run_pending()
        print("Main thread is sleeping")
        time.sleep(3)

if __name__ == "__main__":
    main()