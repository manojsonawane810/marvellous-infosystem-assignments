import schedule
import time

def displayMessage(message):
    print(message)

def main():
    message = input("Enter a message which needs to be dispalyed : ")

    schedule.every(5).seconds.do(displayMessage, message)
    
    while True:
        schedule.run_pending()
        time.sleep(3)

if __name__ == "__main__":
    main()