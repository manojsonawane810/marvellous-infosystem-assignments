def primeNumber(num):
    count = 0;
    for no in range(1, num + 1):
        if num % no == 0:
            count = count + 1
            
    if count == 2:
        print(num, "is prime number")
    else:
        print(num, "is not prime number")

def main():
    num = int(input("Enter number:"))

    primeNumber(num)

if __name__ == "__main__":
    main()