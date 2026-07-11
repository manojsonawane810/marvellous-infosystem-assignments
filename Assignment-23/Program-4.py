import time
import multiprocessing
import os

def countOfOdd(number):
    print(f"Process is running with PID: {os.getpid()} and Parent PID is: {os.getppid()}")

    count = 0
    for no in range(2, number + 1, 2):
        count = count + 1
    return count

def main():
    print(f"Process is running with PID: {os.getpid()}")

    elements = [100000, 200000, 300000, 400000, 500000, 600000]
    
    startTime = time.perf_counter()
    
    oddPool = multiprocessing.Pool()
    result = oddPool.map(countOfOdd, elements)
    
    oddPool.close()
    oddPool.join()
    
    endTime = time.perf_counter()

    print(f"Total time required is : {endTime - startTime:.4f}")
    print("Input elements are: ")
    
    print(elements)
    
    print("\n")
    print("Odd number count: ")
    print(result)

if __name__ == "__main__":
    main()