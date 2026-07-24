import schedule
import datetime
import time

def displayDateAndTime():
    currDateTime = datetime.datetime.now()
    currDateTime = currDateTime.strftime("%d-%m-%Y %I:%M:%S %p")
    print("Current date time is : ", currDateTime)

def main():
    print("Scheduling a task for every 1 minute.")
    schedule.every(2).seconds.do(displayDateAndTime)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()