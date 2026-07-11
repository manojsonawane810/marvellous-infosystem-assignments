import time
import multiprocessing
import os

def primeNumbersTillNum(number):
    print(f"Process is running with PID: {os.getpid()} and Parent PID is: {os.getppid()}")

    primeNumCount = 0

    for num in range(1, number + 1):
        factCount = 0
        
        for no in range(1, num +1):
            if num % no == 0:
                factCount = factCount + 1

        if factCount == 2:
            primeNumCount = primeNumCount + 1

    print(f"Total prime numbers from 1 to {number} are: {primeNumCount}")
    return primeNumCount

def main():
    print(f"Process is running with PID: {os.getpid()}")

    elements = [1000000]

    startTime = time.perf_counter()
    
    primeNumberProcess = multiprocessing.Pool()
    result = primeNumberProcess.map(primeNumbersTillNum, elements)
    
    primeNumberProcess.close()
    primeNumberProcess.join()
    
    endTime = time.perf_counter()

    print(f"Total time required is: {endTime - startTime:.4f}")
    print("Result is: ")
    print(result)

if __name__ == "__main__":
    main()