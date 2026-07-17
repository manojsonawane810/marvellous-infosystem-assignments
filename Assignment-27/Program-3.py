class Numbers:
    
    def __init__(self, value):
        self.value = value
    
    def chkPrime(self):
        count = 0
        
        for no in range(1, self.value + 1):
            if self.value % no == 0:
                count = count + 1
        
        if count == 2:
            return True
        else:
            return False

    def chkPerfect(self):
        sum = 0
        half = self.value // 2
        
        for no in range(1, half):
            if self.value % no == 0:
                sum = sum + no

        sum = sum + half

        if sum == self.value:
            return True
        else:
            return False
    
    def factors(self):
        factorsOfNum = []

        for no in range(1, self.value + 1):
            if self.value % no == 0:
                factorsOfNum.append(no)

        return factorsOfNum

    def sumFactors(self, factorOfNum):
        sum = 0

        for fact in factorOfNum:
            sum = sum + fact
        
        return sum


print("Enter a number to check about number: ")

num = 0

try:
    num = int(input())
    if num <= 0:
        print("Number should be greater than zero")

except ValueError as vError:
    print("Exception occured while entering a number. Please enter valid positive non decimal number. ", vError)

nObj = Numbers(num)
isPrime = nObj.chkPrime()
isPerfect = nObj.chkPerfect()
factorsOfNum = nObj.factors()
sumOfFact = nObj.sumFactors(factorsOfNum)

if isPrime:
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")

if isPerfect:
    print(f"{num} is perfect number")
else:
    print(f"{num} is not perfect number")

print(f"Factors of number {num} are {factorsOfNum}")
print(f"Sum of factors of number {num} is: ", sumOfFact)


print("Enter a number to check about number: ")

num = 0

try:
    num = int(input())
    if num <= 0:
        print("Number should be greater than zero")

except ValueError as vError:
    print("Exception occured while entering a number. Please enter valid positive non decimal number. ", vError)



nObj1 = Numbers(num)
isPrime = nObj1.chkPrime()
isPerfect = nObj1.chkPerfect()
factorsOfNum = nObj1.factors()
sumOfFact = nObj1.sumFactors(factorsOfNum)

if isPrime:
    print(f"{num} is prime number")
else:
    print(f"{num} is not prime number")

if isPerfect:
    print(f"{num} is perfect number")
else:
    print(f"{num} is not perfect number")

print(f"Factors of number {num} are {factorsOfNum}")
print(f"Sum of factors of number {num} is: ", sumOfFact)