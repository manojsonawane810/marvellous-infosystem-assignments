import time
import multiprocessing
import os

def factorialsOfNum(number):
    print(f"Process is running with PID: {os.getpid()} and Parent PID is: {os.getppid()}")

    fact = 1
    for i in range(1, number + 1):
        fact = fact * i
    return fact

def main():
    print(f"Process is running with PID: {os.getpid()}")

    elements = [10, 15, 20, 25, 30, 38]
    
    startTime = time.perf_counter()
    
    factorial = multiprocessing.Pool()
    result = factorial.map(factorialsOfNum, elements)
    
    factorial.close()
    factorial.join()
    
    endTime = time.perf_counter()

    print(f"Total time required is: {endTime - startTime:.4f}")
    print("Input elements are: ")
    
    print(elements)
    
    print("\n")
    print("Result is: ")
    print(result)

if __name__ == "__main__":
    main()