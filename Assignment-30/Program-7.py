import schedule
import os
import datetime
import time
import shutil

logFileName = "Backup_log.txt"
border = "-"*40

def logBackUpDetails(message):
    datetimeVal = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    
    if os.path.exists(logFileName) == False:
        fObj = open(logFileName, "w")
    else:
        fObj = open(logFileName, "a")
    
    if message.find("backed", 0, (len(message) - 1)) > -1 :
        fObj.write(border+"\n")

    fObj.write(message + " at " + datetimeVal + "\n")

    if message.find("completed", 0, (len(message) - 1)) > -1:
        fObj.write(border+"\n")

def giveDateAndTimeString():
    datetimeVal = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    datetimeVal = datetimeVal.replace("-", "_")
    datetimeVal = datetimeVal.replace(" ", "_")
    datetimeVal = datetimeVal.replace(":", "_")
    return datetimeVal

def doBackup(sourceFile, destination):
    try:
    
        print(border)
        os.chdir(destination)
        path = shutil.copy(sourceFile, destination)
        logBackUpDetails("Source file has been backed up to destination folder")

        fileName, fileExtension = os.path.splitext(path)
        backupFileName = os.path.basename(fileName)

        datetimeVal = giveDateAndTimeString()

        os.rename(path, backupFileName + "_" + datetimeVal + fileExtension)
        logBackUpDetails("Source filename has been renamed")
        logBackUpDetails("Back up completed successfully")
        print(border)
    
    except Exception as eObj:
        print("Exception occured during file backup. ", eObj)


def main():
    print(border)
    print("Scheduling task to take file backup...")
    
    filePath = input("Enter the source file name with absolute path to be backed up : ")
    destPath = input("Enter the directory path to back up the file in the given directory : ")

    if os.path.exists(filePath) == False or os.path.isfile(filePath) == False:
        print("File does not exist. Please check file exist or not")
        return

    if os.path.exists(destPath) == False:
        print("Direcory does not exist. It is being created by system for backup")
        os.makedirs(destPath,777)
    
    schedule.every().hour.do(doBackup, filePath, destPath)

    while True:
        schedule.run_pending()
        print("Main thread is going to sleep for some time...")
        time.sleep(15*60)
    

if __name__ == "__main__":
    main()