import threading
import time

def addition(elements):
    print("Addition thread id is: ", threading.get_ident() ," Thread name is: ", threading.current_thread().name)
    sum = 0
    for no in elements:
        sum = sum + no
    return sum

def evenList(*elements):
    print("Even list thread ID is: ", threading.get_ident() ," Thread name is: ", threading.current_thread().name)
    evenNumbers = []
    for num in elements:
        if num % 2 == 0:
            evenNumbers.append(num)

    print("Even number list: ", evenNumbers)
    evenAdd = addition(evenNumbers) 
    print("Addition of even numbers is: ", evenAdd)

def oddList(*elements):
    print("Odd list thread Id is: ", threading.get_ident() ," Thread name is: ", threading.current_thread().name)
    oddNumbers = []
    for num in elements:
        if num % 2 != 0:
            oddNumbers.append(num)

    print("Odd number list: ", oddNumbers)
    oddAdd = addition(oddNumbers) 
    print("Addition of odd numbers is: ", oddAdd)

def main():
    print("Main thread id is: ", threading.get_ident() ," Thread name is: ", threading.current_thread().name)
    startTime = time.perf_counter()
    evenListThread = threading.Thread(target=evenList, args=(2,4,3,5,7,8,9,10,15,17,19,22,44,33,62,78,88,90,91,35,61,57,))
    oddListThread = threading.Thread(target=oddList, args=(2,4,3,5,7,8,9,10,15,17,19,22,44,33,62,78,88,90,91,35,61,57,))
    
    evenListThread.start()
    oddListThread.start()

    evenListThread.join()
    oddListThread.join()


    endTime = time.perf_counter()

    print(f"Time required is: {endTime - startTime:.4f}")

if __name__ == "__main__":
    main()