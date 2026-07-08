import threading

## Thread2 started after Thread1 ended using while loop

def displayNumbers():
    print("displayNumbers thread ID is: ", threading.get_ident() , " and thread name is: ", threading.current_thread().name)
    sum = 0
    for i in range(1, 51000):
        sum = sum + i ** 11
        print(sum, end="\t")
    
    print("\n")

def displayNumbersInReverse():
    print("displayNumbersInReverse thread ID is: ", threading.get_ident() , " and thread name is: ", threading.current_thread().name)

    for i in range(50, 0, -1):
        print(i, end="\t")
    
    print("\n")

def main():
    print("Main thread ID is: ", threading.get_ident() , " and thread name is: ", threading.current_thread().name)

    thread1 = threading.Thread(target=displayNumbers, name="Thread1")
    thread2 = threading.Thread(target=displayNumbersInReverse, name="Thread2")

    thread1.start()
    thread1.join()        
    
    thread2.start()
    thread2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()