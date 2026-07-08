import threading
from functools import reduce

def maxNumber(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

def minNumber(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2
    
def displayMaxNumber(numbers):
    print(f"{threading.current_thread().name} thread ID is: {threading.get_ident()}")
    
    max = reduce(maxNumber, numbers)
    print(f"Maximum numbers is: {max}")

def displayMinNumber(numbers):
    print(f"{threading.current_thread().name} thread ID is: {threading.get_ident()}")
    
    min = reduce(minNumber, numbers)
    print(f"Minimum numbers is: {min}")

def main():
    print(f"{threading.current_thread().name} thread ID is: {threading.get_ident()}")

    elementCount = int(input("Enter number of elements: "))
    numbers = []
    
    for i in range(elementCount):
        no = int(input("Enter a number: "))
        numbers.append(no)

    thread1 = threading.Thread(target=displayMaxNumber, args=(numbers,))
    thread1.name = "Max-Thread1"
    thread2 = threading.Thread(target=displayMinNumber, args=(numbers,))
    thread2.name = "Min-Thread2"

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()