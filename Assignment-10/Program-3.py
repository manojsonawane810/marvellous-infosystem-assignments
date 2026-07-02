def factorialOfNumber(num):
    # Using for loop
    factorial = 1
    for i in range(num, 0, -1):
         factorial = factorial * i

    print("Factorial of number is : ", factorial)     

    # Using while loop
    fact = 1
    while num > 1:
        fact = fact * num
        num = num - 1

    print("Factorial of number is: ", fact)

def main():
    num = int(input("Enter a number: "))
    factorialOfNumber(num)

if __name__ == "__main__":
    main()