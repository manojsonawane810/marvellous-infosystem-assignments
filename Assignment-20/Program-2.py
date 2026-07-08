from functools import reduce
import threading

#sumEven = lambda num1, num2 : num1 + num2
#sumOdd = lambda num1, num2 : num1 + num2
#sum = lambda num1, num2 : num1 + num2 

# Question: will this create a race condition or deadlock while accessing same resource by 2 threads?
# do we need synchronization? 

def sum(num1, num2):
    print("Sum thread ID is: ", threading.get_ident())
    return num1 + num2

def evenFactors(num):
    print("Evenfactors thread ID is: ", threading.get_ident())
    evenFactors = []

    for i in range(2, num, 2):
        if num % i == 0:
            evenFactors.append(i)
    print(f"Even factors of {num} are: ", evenFactors)

    sumOfEven = reduce(sum, evenFactors)

    print("Addition of even factors is: ", sumOfEven)

def oddFactors(num):
    print("Oddfactors thread ID is: ", threading.get_ident())
    oddFactors = []
    print(type(num))
    for i in range(1, num, 2):
        if num % i == 0:
            oddFactors.append(i)
    print(f"Odd factors of {num} are: ", oddFactors)

    sumOfOdd = reduce(sum, oddFactors)

    print("Addition of odd factors is: ", sumOfOdd)

def main():
    print("Main thread ID is: ", threading.get_ident())
    evenFactor = threading.Thread(target=evenFactors, args=(400000,))
    oddFactor = threading.Thread(target=oddFactors, args=(330000,))
    #evenFactor(40)
    #oddFactor(33)

    evenFactor.start()
    oddFactor.start()

    evenFactor.join()
    oddFactor.join()

    print("Exit from main")

if __name__ == "__main__":
    main()