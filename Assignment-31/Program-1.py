import schedule
import time

def displayMessage(message):
    print(message + "\n")

def main():
    message = input("Enter a message which needs to be dispalyed : ")
    interval = int(input("Enter time interval for scheduling message display : "))

    if interval < 0:
        print("Time interval should be greater than 0")
    
    schedule.every(interval).seconds.do(displayMessage, message)
    sleepTime = interval // 2

    while True:
        schedule.run_pending()
        time.sleep(sleepTime)

if __name__ == "__main__":
    main()