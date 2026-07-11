import time
import multiprocessing
import os

def sumOfEven(number):
    print(f"Process is running with PID: {os.getpid()} and Parent PID is: {os.getppid()}")

    sum = 0
    for no in range(1, number + 1):
        if no % 2 == 0:
            sum = sum + no
    return sum

def main():
    print(f"Process is running with PID: {os.getpid()}")

    elements = [100000, 200000, 300000, 400000, 500000, 600000]
    
    startTime = time.perf_counter()
    
    evenPool = multiprocessing.Pool()
    result = evenPool.map(sumOfEven, elements)
    
    evenPool.close()
    evenPool.join()
    
    endTime = time.perf_counter()

    print(f"Total time required is: {endTime - startTime:.4f}")
    print("Input elements are: ")
    
    print(elements)
    
    print("\n")
    print("Sum of even numbers : ")
    print(result)

if __name__ == "__main__":
    main()