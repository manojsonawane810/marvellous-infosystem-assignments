import schedule
import os
import datetime
import time
import shutil

logFileName = "Backup_log.txt"
border = "-"*40

def logTotalCopiedFilesDetails(copiedFileCount):
    if os.path.exists(logFileName) == False:
        fObj = open(logFileName, "w")
    else:
        fObj = open(logFileName, "a")
        
    fObj.write(border+"\n")
    fObj.write(f"Total files copied : {copiedFileCount} \n")
    fObj.write(border+"\n")

def logBackUpDetails(filepath, destDir):
    datetimeVal = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    
    if os.path.exists(logFileName) == False:
        fObj = open(logFileName, "w")
    else:
        fObj = open(logFileName, "a")
    
    fObj.write(border+"\n")
    fObj.write(f"Source file {filepath} has been copied to destination folder {destDir} at " + datetimeVal + "\n")
    fObj.write(border+"\n")

def doBackup(sourceDir, destDir):
    try:
        print("Back up job started")
        if os.path.exists(sourceDir) == False or os.path.exists(destDir) == False:
                print("Source or destination directory does not exist, please check!")
                return
        
        print(border)
        copiedFileCount = 0
        for folders, subfolders, files in os.walk(sourceDir):
            for fileObj in files:
                fileName, fileExtension = os.path.splitext(fileObj)
                if fileExtension == ".txt":
                    fName = os.path.join(folders, fileObj)
                    print(fName)
                    filepath = shutil.copy(fName, destDir)
                    copiedFileCount = copiedFileCount + 1
                    logBackUpDetails(filepath, destDir)

        logTotalCopiedFilesDetails(copiedFileCount)  
        print("Back up job completed successfully")
        print(border)
    
    except Exception as eObj:
        print("Exception occured during file backup. ", eObj)


def main():
    print(border)
    print("Scheduling task to take file backup...")
    
    sourceDir = input("Enter the source directory name with absolute path to copy files from : ")
    destDir = input("Enter the destination directory to be used for copying files to : ")

    if os.path.exists(sourceDir) == False or os.path.exists(destDir) == False:
        print("Source or destination directory does not exist, please check!")
        return
    
    schedule.every(10).minutes.do(doBackup, sourceDir, destDir)

    while True:
        schedule.run_pending()
        print("Main thread is going to sleep for some time...")
        time.sleep(7 * 60)
    

if __name__ == "__main__":
    main()