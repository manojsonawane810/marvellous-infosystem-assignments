def isPrimeNumber(num):
    divisibleCount = 0

    for i in range(1, num + 1):
        if num % i == 0:
            divisibleCount = divisibleCount + 1

    if divisibleCount == 2:
        print(f"Number {num} is prime")
    else:
        print(f"Number {num} is not prime")    

def main():
    num = int(input("Enter a number: "))
    isPrimeNumber(num)

if __name__ == "__main__":
    main()