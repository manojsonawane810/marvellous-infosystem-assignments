import schedule
import time

def lunchTime():
    print("Lunch Time!")

def leaveTime():
    print("Wrap up work!")

def main():
    print("Scheduling office task for everyday.")
    schedule.every().days.at("13:00").do(lunchTime)
    schedule.every().days.at("18:00").do(leaveTime)

    while True:
        schedule.run_pending()
        time.sleep(60 * 60)

if __name__ == "__main__":
    main()