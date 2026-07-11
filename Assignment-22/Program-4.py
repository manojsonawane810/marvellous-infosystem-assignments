import time
import multiprocessing
import os


def powerOfNum(number):
    print(f"Process is running with PID: {os.getpid()} and Parent PID is: {os.getppid()}")

    sumOfPower = 0

    for no in range(1, number + 1):
        sumOfPower = sumOfPower + no ** 5
    

    print(f"Sum of power of all numbers is : {sumOfPower}")
    
    return sumOfPower

def main():
    print(f"Process is running with PID: {os.getpid()}")

    
    elements = [10000,20000,30000,40000,50000]

    startTime = time.perf_counter()
    
    powerCalcProcess = multiprocessing.Pool()
    result = powerCalcProcess.map(powerOfNum, elements)
    
    powerCalcProcess.close()
    powerCalcProcess.join()
    
    endTime = time.perf_counter()

    print(f"Total time required is: {endTime - startTime:.4f}")
    print("Result is: ")
    print(result)

if __name__ == "__main__":
    main()