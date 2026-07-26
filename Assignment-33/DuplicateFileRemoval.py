##################################################################
#
#   Importing required libraries
#
##################################################################

import sys
import os
import time
import schedule
import datetime
import EmailSender as mailSender

from checksumlib import calculateChecksum


########################################################################
#
# run using following command
#
# python DuplicateFileRemoval.py D:\Marvellous-Infosystems\Assignment-33\SourceDir 1 marvellousinfosystem@gmail.com
#
#########################################################################

border = "-"*50

def prepareNotification(receiver, body, logFileName):
    senderEmail = "codeautomatorsender@gmail.com"
    subject = "Duplicate file removal statistics"
    attachment = logFileName
    emailObj = mailSender.prepareNotification(senderEmail, receiver, subject, body, attachment)
    return emailObj

def prepareEmailBody(startTime, dirName, totalFilesScanned, totalDuplicateFiles, totalDeletedFiles, endTime):
    emailBody = f"""
        Jay Ganesh,

        The duplicate file removal operation has been completed successfully.

        Operation statistics:

        Starting time of scanning: {startTime}
        Completion time of scanning: {endTime}
        Directory scanned: {dirName}
        Total number of files scanned: {totalFilesScanned}
        Total number of duplicate files found: {totalDuplicateFiles} 
        Total number of duplicate files found: {totalDeletedFiles}

        Please find the detailed log file attached to this email.

        Regards,
        Marvellous Automation System
    """

    return emailBody

def getFiles(duplicateFilesList):
    removedFilesList = []
    for duplicateFiles in duplicateFilesList:
        for removedFile in duplicateFiles:
            removedFilesList.append(removedFile)
    return removedFilesList

def sendNotification(emailObj):
    appPassword = "veky udpg hqut ytlk"
    mailSender.sendMail(emailObj, appPassword)
   
    
def logDeletedFiles(lObj, deletedFilesMap):
    for deletedFileKey in deletedFilesMap.keys():
        deletedFiles = deletedFilesMap.get(deletedFileKey)
        if len(deletedFiles) > 0:
            for file in deletedFiles:
                addLog(lObj, "Checksum value of deleted file : ", deletedFileKey)
                addLog(lObj, "Abosulte path of deleted file : ", file)
        

def addBorderLog(lObj):
    lObj.write(border + "\n")

def addLog(lObj, message, value):
    lObj.write(f"{message} {value} \n")

def formattedDatTimeString(dateTimeVal):
    dateTimeVal = dateTimeVal.replace(" ", "_")
    dateTimeVal = dateTimeVal.replace(":", "_")
    dateTimeVal = dateTimeVal.replace("-", "_")
    return dateTimeVal

def createLogFile(logDirectoryName):
    if os.path.exists(logDirectoryName) == False:
        print("Log directory ", logDirectoryName , " does not exist.")
        return
    
    logFileName = "DuplicateRemovalLog.log"

    datateTimeVal = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    datateTimeVal = formattedDatTimeString(datateTimeVal)

    filename, fileextension = os.path.splitext(logFileName)
    logFileName = filename + "_"+ datateTimeVal + fileextension

    #os.chdir(logDirectoryName)
    logFileName = os.path.join(logDirectoryName, logFileName)

    if os.path.exists(logFileName) == False:
        lObj = open(logFileName, "w")
    else:
        lObj = open(logFileName, "a")

    return logFileName, lObj
       

def createLogDirectory():
    logDirectoryName = "Marvellous"

    if os.path.exists(logDirectoryName) == False:
        os.mkdir(logDirectoryName)
    
    return os.path.abspath(logDirectoryName)

def removeDuplicateFiles(duplicateFilesMap, lObj):
    deletedFilesMap = {}
    
    if len(duplicateFilesMap) > 0:
        for keyVal in duplicateFilesMap.keys():
            deletedFiles = []
            duplicateFileNames = duplicateFilesMap.get(keyVal)
           
            for duplicateFile in duplicateFileNames:
                try:
                    if os.path.exists(duplicateFile) == True:
                        os.remove(duplicateFile)
                        deletedFiles.append(duplicateFile)
                        deletedFilesMap[keyVal] = deletedFiles
                    else:
                        addLog(lObj, "Duplicate file does not exist now or deleted : ", duplicateFile)
                                    
                except Exception as eObj:
                    addLog(lObj, "Exception occured while removing duplicate files : ", eObj)                    
                
    return deletedFilesMap

def scanDirectoryAndGetDuplicateFiles(dirName):
    uniqueFilesMap = {}
    duplicateFilesMap = {}
    totalFilesScanned = 0

    for folderName, subfolders, fileNames in os.walk(dirName):
        for fileName in fileNames:
            totalFilesScanned = totalFilesScanned + 1
            fileName = os.path.join(folderName, fileName)
            if os.path.getsize(fileName) > 0:
                checksumValue = calculateChecksum(fileName)
                if uniqueFilesMap.__contains__(checksumValue) == False:
                    uniqueFilesMap.update({checksumValue : fileName})
                else:                
                    if duplicateFilesMap.__contains__(checksumValue) == False:
                        duplicateFilesMap.update({checksumValue : [fileName]}) 
                        #duplicateFilesMap[checksumValue] = [fileName]
                    else:
                        duplicateFiles = duplicateFilesMap.get(checksumValue)
                        duplicateFiles.append(fileName)
                        duplicateFilesMap[checksumValue] = duplicateFiles

    return totalFilesScanned, duplicateFilesMap   

def executeFileRemovalProcess(dirName, receiver, scriptName):
    logFileName, lObj = createLogFile("Marvellous")

    addLog(lObj, "Welcome to the duplicate file removal automation...", scriptName)
    startTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%Y %p")

    addBorderLog(lObj)
    addLog(lObj, "Starting time of directory scanning ", startTime)

    totalFilesScanned, duplicateFilesMap = scanDirectoryAndGetDuplicateFiles(dirName)

    addLog(lObj, "Name of the directory scanned : ", dirName)
    addLog(lObj, "Total number of files scanned : ", totalFilesScanned)
    
    duplicateFilesList = getFiles(duplicateFilesMap.values())

    deletedFilesMap = removeDuplicateFiles(duplicateFilesMap, lObj)

    removedFilesList = getFiles(deletedFilesMap.values())
    
    addLog(lObj, "Total number of duplicate files found : ", len(duplicateFilesList))

    addLog(lObj, "Total number of duplicate files deleted : ", len(removedFilesList))

    logDeletedFiles(lObj, deletedFilesMap)

    endTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%Y %p")

    addLog(lObj, "Completion time of directory scanning ", endTime)

    emailBody = prepareEmailBody(startTime, dirName, totalFilesScanned, len(duplicateFilesList), len(removedFilesList), endTime)
    emailObj = prepareNotification(receiver, emailBody, logFileName)    
    sendNotification(emailObj)
    addLog(lObj, "Automatic email notification with files statistics has been sent to the receiver ", receiver)

    addBorderLog(lObj)

    lObj.close()

def main():

    logDirectoryName = createLogDirectory()
    logFileName, lObj = createLogFile(logDirectoryName)

    if len(sys.argv) != 4:
        addLog(lObj, "Invalid number of command line arguments, please check. Required : ", len(sys.argv))
        return
    
    dirName = sys.argv[1]
    runInterval = 0
    try:
        runInterval = int(sys.argv[2])
    except Exception as eObj:
        addLog(lObj, "Exception while casting command line argument for time interval in minutes, please provide interger value ", eObj)
        return

    emailReciever = sys.argv[3]

    
    if runInterval <= 0:
        addLog(lObj, "Time interval should be greater than zero (0) ", runInterval)
        return
    
    if os.path.exists(dirName) == False or os.path.isdir(dirName) == False:
        addLog(lObj, "Directory does not exist, please check.", dirName)
        return

    schedule.every(runInterval).minutes.do(executeFileRemovalProcess, dirName, emailReciever, sys.argv[0])
    
    #executeFileRemovalProcess(dirName, emailReciever, logFileName, lObj)
    sleepTime = runInterval // 2

    while True:
        schedule.run_pending()
        time.sleep(sleepTime)

if __name__ == "__main__":
    main()