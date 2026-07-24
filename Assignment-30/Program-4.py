import schedule
import time

def printNamaskar():
    print("Namaskar...")

def main():
    print("Scheduling a task for every morning at 9 AM")
    schedule.every().day.at("09:00").do(printNamaskar)

    while True:
        schedule.run_pending()
        print("Sleeping main thread for some time")
        # sleping for 30 minutes
        time.sleep(30 * 60 )


if __name__ == "__main__":
    main()