import time
import multiprocessing
import os

def squareOfNum(num):
    return num * num

def sumOfSquaresOfNum(number):
    print(f"Process is running with PID: {os.getpid()} and Parent PID is: {os.getppid()}")

    sum = 0
    for i in range(1, number + 1):
        sqaure = squareOfNum(i)
        sum = sum + sqaure
    return sum

def main():
    print(f"Process is running with PID: {os.getpid()}")

    elements = [1000000, 2000000, 3000000, 4000000, 5000000000]
    
    startTime = time.perf_counter()
    
    sumSquare = multiprocessing.Pool()
    result = sumSquare.map(sumOfSquaresOfNum, elements)
    
    sumSquare.close()
    sumSquare.join()
    
    endTime = time.perf_counter()

    print(f"Total time required is: {endTime - startTime:.4f}")
    print("Result is: ")
    print(result)

if __name__ == "__main__":
    main()