import schedule
import time

def printMessage():
    print("Coding Kar...!")

def main():
    print("Scheduling a task to print a message")
    schedule.every(30).minutes.do(printMessage)

    while True:
        schedule.run_pending()
        print("Main thread is sleeping now.")
        time.sleep(15*60)
    

if __name__ == "__main__":
    main()