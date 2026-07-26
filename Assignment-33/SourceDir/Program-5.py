import schedule
import datetime
import time
import os

def generateLogs(fObj, deletedFiles, dirName):
    border = "-"*40
    dateTimeVal = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    fObj.write(border + "\n")
    fObj.write(f"Total {len(deletedFiles)} number of files are deleted from parent directory {dirName} \n\n")
    if len(deletedFiles) > 0 :
        fObj.write("Below is the list of deleted files :")

        for deletedFile in deletedFiles:
            fObj.write(deletedFile + "\n")

    fObj.write("Scan completed on : " + dateTimeVal + "\n")
    fObj.write(border + "\n")
    

def logFileNameCreation():
    logFileName = "DirectoryScanningLog.txt"

    if os.path.exists(logFileName) == False:
        fObj = open(logFileName, "w")
    else:
        fObj = open(logFileName, "a")

    return fObj

def directoryScan(dirName):
    print("Scanning diretory started...")
    try:
        if os.path.exists(dirName) == True and os.path.isdir(dirName) == True :
            emptyfiles = []
            print("Dir: ", dirName)    
            for foldernames, subfolders, filenames in os.walk(dirName):
                for filename in filenames:
                    filename = os.path.join(foldernames, filename)
                    if os.path.getsize(filename) == 0:
                        emptyfiles.append(filename)
                        os.remove(filename)
            print("Dir: ", dirName)                
            fObj = logFileNameCreation()

            generateLogs(fObj, emptyfiles, dirName)    
        
        else :
            print("Specified directory does not exist.")
            print("Scanning diretory completed...")
            return
        
    except Exception as eObj:
        print("Error occured while scanning the directory, please check the file access or directory existance.", eObj)
    
    print("Scanning diretory completed...")
    
def main():
    print("Scheduling a directory scanning...")

    dirName = "D:\\Marvellous-Infosystems\\Assignment-32\\TestDir"

    if os.path.isdir(dirName) == False or os.path.exists(dirName) == False:
        print("Invalid directory name")
        return
    else :
        schedule.every().hour.do(directoryScan, dirName)
    
        while True:
            schedule.run_pending()
            print("Main thread is sleeping...")
            time.sleep(45 * 60)

if __name__ == "__main__":
    main()