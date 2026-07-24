import schedule
import datetime
import time
import os

def generateLogs(fObj, noOfFiles, dirName):
    border = "-"*40
    dirPathName = os.path.dirname(dirName)
    dateTimeVal = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    fObj.write(border + "\n")
    fObj.write("Directory parent path is : " + dirPathName + "\n")
    fObj.write("Directory is : " + dirName + "\n")    
    fObj.write(f"Total number of files in directory are :  {noOfFiles} \n")
    fObj.write("Date and time is : " + dateTimeVal + "\n")
    fObj.write(border + "\n")
    

def logFileNameCreation():
    logFileName = "DirectoryCountLog.txt"

    if os.path.exists(logFileName) == False:
        fObj = open(logFileName, "w")
    else:
        fObj = open(logFileName, "a")

    return fObj

def countFilesInDirectory(dirName):
    print("Scanning diretory started...")

    fileCount = 0
    if os.path.isdir(dirName) == True and os.path.exists(dirName) == True:
        for foldernames, subfolders, filenames in os.walk(dirName):        
            for filename in filenames:
                fileCount = fileCount + 1
    
        fObj = logFileNameCreation()
    
        generateLogs(fObj, fileCount, dirName)
    
    else:
        print("Directory does not exist.")
        return
    
    
    print("Scanning diretory completed...")
    
def main():
    print("Scheduling a directory scanning...")

    dirName = input("Enter a directory name with aboslute path : ")

    if os.path.isdir(dirName) == False or os.path.exists(dirName) == False:
        print("Invalid directory name")
        return
    else :
        schedule.every(5).minutes.do(countFilesInDirectory, dirName)
    
        #countFilesInDirectory(dirName)

    while True:
        schedule.run_pending()
        print("Main thread is sleeping...")
        time.sleep(3 * 60)

if __name__ == "__main__":
    main()