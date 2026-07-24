import schedule
import time


def mondayMessageTask():
    mondayMessage = "Start your weekly goals"
    print(mondayMessage)

def wedMessageTask():
    wedMessage = "Review your weekly progress"
    print(wedMessage)

def fridayMessageTask():
    fridayMessage = "Weekly work completed"
    print(fridayMessage)

def main():
    print("Scheduling weekly TODO list..")    

    print("Scheduling monday message task at 9:00 AM")
    schedule.every().monday.at("09:00").do(mondayMessageTask)

    print("Scheduling wednesday message task at 5:00 PM")
    schedule.every().wednesday.at("17:00").do(wedMessageTask)

    print("Scheduling friday message task at 6:00 PM")
    schedule.every().friday.at("18:00").do(fridayMessageTask)

    while True:
        schedule.run_pending()
        print("Main thread is sleeping...")
        time.sleep(4 * 60 * 60)

if __name__ == "__main__":
    main()