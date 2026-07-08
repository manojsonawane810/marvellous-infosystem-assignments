import threading
import time

def displayEven():
    print("displayEven thread is running and ID is: ", threading.get_ident())
    print("\n")
    for i in range(2, 21, 2):
        print(i, end="\t")
    
    print("\n")
    print("displayEven thread completed.")
    print("-"*40)

def displayOdd():
    print("displayOdd thread is running and ID is: ", threading.get_ident(), end="\n")
    print("\n")
    for i in range(1, 20, 2):
        print(i, end="\t")

    print("\n")
    print("displayOdd thread completed.")
    print("-"*40)

def main():
    print("The main thread is running and ID is: ", threading.get_ident())
    print("\n")
    startTime = time.perf_counter()
    thread1 = threading.Thread(target=displayEven)
    thread2 = threading.Thread(target=displayOdd)
    

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
   
    endTime = time.perf_counter()
    print(f"The main thread is completed. Time required to complete the task is : {endTime - startTime:.4f}")

if __name__ == "__main__":
    main()