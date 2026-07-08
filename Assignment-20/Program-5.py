import threading

def displayNumbers():
    print("displayNumbers thread ID is: ", threading.get_ident() , " and thread name is: ", threading.current_thread().name)
    for i in range(1, 51):
        print(i, end="\t")
    print("\n")

def displayNumbersInReverse(thread):
    thread.join()
    print(f"{thread.name} has completed")
    print("displayNumbersInReverse thread ID is: ", threading.get_ident() , " and thread name is: ", threading.current_thread().name)

    if thread.is_alive() == False:
        for i in range(50, 0, -1):
            print(i, end="\t")
    else:
        print(f"{thread.name} is alive")
    print("\n")

def main():
    print("Main thread ID is: ", threading.get_ident() , " and thread name is: ", threading.current_thread().name)

    thread1 = threading.Thread(target=displayNumbers, name="Thread1")
    thread2 = threading.Thread(target=displayNumbersInReverse, name="Thread2", args=(thread1,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()