import schedule
import time

def printMessage():
    print("Jay Ganesh...")


def main():
    print("Scheduling a task for every 2 seconds.")
    schedule.every(2).seconds.do(printMessage)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()