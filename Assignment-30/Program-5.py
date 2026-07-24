import time
import schedule
import datetime
import os

def writeData():
    fileName = "Marvellous.txt"
    
    if os.path.exists(fileName):
        fObj = open(fileName, "a")
    else:
        fObj = open(fileName, "w")

    currentTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")    
    fObj.write("Task executed at : " + currentTime + "\n")

    fObj.close()

def main():
    print("Scheduling a task to write the current date in file")
    schedule.every(5).minutes.do(writeData)

    while True:
        schedule.run_pending()
        print("Sleeping main thread for some time.")
        time.sleep(3 * 60)

if __name__ == "__main__":
    main()