import psutil
import sys
import os
import time
import schedule

def processesScanning(processName):
    listProcesses = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["name", "status"])
        pName, pExtension = os.path.splitext(info.get("name"))
        
        if pName == processName.lower() or pName == processName.upper():
            listProcesses.append(info)
    
    return listProcesses


def searchProcessStatus(processName, logFolder):
    border = "-"*70
    print(border)
    print("Process searching is started")
    print(border)

    if os.path.exists(logFolder) == True:
        if os.path.isdir(logFolder) == False:
            print("Directory name exists but its not a directory")
    else:
        os.mkdir(logFolder)
        print("Log directory is created.")

    timeVal = time.strftime("%d-%m-%Y_%I-%M-%S-%p")
    logfile = os.path.join(logFolder, "ProcLogs-%s.log" %timeVal)
    fObj = open(logfile, "w")

    print("Log files created successfully")

    fObj.write(border+"\n")
    fObj.write("---------------- Process searching Automation System ----------------\n")
    fObj.write(f"Log file created at {timeVal} \n")
    fObj.write(border+"\n\n")

    fObj.write("---------------- Process Scanned Report ----------------\n")

    listProcesses = processesScanning(processName)

    if len(listProcesses) == 0:
        print(f"Process {processName} does not exist or is created\n")
        fObj.write(f"Process {processName} does not exist or is created\n")
    else:
        for proc in listProcesses:
            fObj.write(f"{proc}\n")
            fObj.write(border+"\n")
            if proc.get("status") == "running":
                print(f"{processName} is running!")
                break
            
            
    fObj.write(border+"\n")
    fObj.write("---------------- End of Log file ----------------\n")
    fObj.write(border+"\n")

def main():
    border = "-"*70
    print(border)
    print("Process Searching system")
    print(border)



    if len(sys.argv) == 2:
        if sys.argv[1] == "--h" or sys.argv[1] == "--H":
            print("This automation script is used to search given process and check if running")
            print("Display if process in running or not")
            print("It will generate the log file and store status in it")
            print("This script takes 3 arguments, first is process name, time interval to scan the processes every specified interval and name of directory to create log files in it")
            return
        
        elif sys.argv[1] == "--u" or sys.argv[1] == "--U":
            print("Use the automation script as")
            print("python <Name of python script> <process_name> <time_interval> <log_directory>, eg. as belows")
            print("process_name : name of running process to be searched")
            print("time_interval : time in minutes to process the script in some intervals")
            print("log_directoy: name of directory to store the logs files. Log direcroy will be created if does not exist already")
            print("python ProcInfo-Program-2.py Notepad 2 ProcLogs")
            return
        
        else:
            print("Invalid number of aruguments")
            print("Unable to proceed due to no matching arguments")
            print("Please use --h or --u for more details")
            return
        
    elif len(sys.argv) == 4:
        interval = 0

        try:
            interval = int(sys.argv[2])
        except ValueError as vObj:
            print("Time interval should be interger number without decimal point ", vObj)
            return

        if interval < 1:
            print("Time interval should be greater than 0")
            return 

        #searchProcessStatus(sys.argv[1], sys.argv[3])
        schedule.every(interval).minutes.do(searchProcessStatus, sys.argv[1], sys.argv[3])

    else:
        print("Invalid number of aruguments")
        print("Unable to proceed due to no matching arguments")
        print("Please use --h or --u for more details")
        return

    sleeptime = int(sys.argv[1]) / 2

    while True:
        schedule.run_pending()
        time.sleep(sleeptime)

if __name__ == "__main__":
    main()