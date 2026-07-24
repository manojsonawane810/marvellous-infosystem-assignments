import schedule
import datetime
import time
import os

def scanDirectory(directory):
    print("Scanning the diretory ", directory)

    subfolderCount = 0
    fileCount = 0

    for foldernames, subfolders, filenames in os.walk(directory):
        
        for subfolder in subfolders:
            subfolderCount = subfolderCount + 1
        
        for filename in filenames:
            fileCount = fileCount + 1
    
    dateTimeVal = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")
    
    print("Directory scanned is : ", directory)
    
    print("Total number of files scanned are : ", fileCount)
    print("Total number of subfolders scanned are : ", subfolderCount)
    print("Scan time is : ", dateTimeVal)

def main():
    print("Scheduling a directory scanning...")
    dirName = "D:\\Marvellous-Infosystems\\Assignment-31\\TestDir"
    
    if os.path.isdir(dirName) == False:
        print("Invalid directory.")
    else :
        schedule.every().minute.do(scanDirectory, dirName)
    
    #scanDirectory(dirName)

    while True:
        schedule.run_pending()
        time.sleep(40)

if __name__ == "__main__":
    main()