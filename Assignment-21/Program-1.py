import threading

def primeNumber(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        return True
    else:
        return False

def nonPrimeNumber(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count = count + 1
    if count != 2:
        return True
    else:
        return False
    
def displayPrimeNumbers(*numbers):
    print(f"{threading.current_thread().name} thread ID is: {threading.get_ident()}")
    
    primeNumbers = list(filter(primeNumber, numbers))
    print(f"Prime numbers are: {primeNumbers}")

def displayNonPrimeNumbers(*numbers):
    print(f"{threading.current_thread().name} thread ID is: {threading.get_ident()}")
    
    nonPrimeNumbers = list(filter(nonPrimeNumber, numbers))
    print(f"Non prime numbers are: {nonPrimeNumbers}")

def main():
    print(f"{threading.current_thread().name} thread ID is: {threading.get_ident()}")

    thread1 = threading.Thread(target=displayPrimeNumbers, args=(1,2,4,5,6,788,11,22,12,34,35,56,67,87,65,54,43,90,98,87,67,))
    thread1.name = "Prime"
    thread2 = threading.Thread(target=displayNonPrimeNumbers, args=(1,2,4,5,6,788,11,22,12,34,35,56,67,87,65,54,43,90,98,87,67,))
    thread2.name = "NonPrime"

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()