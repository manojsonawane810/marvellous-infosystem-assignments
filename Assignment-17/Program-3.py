def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

def main():
    num = int(input("Enter a number: "))
    ret = factorial(num)
    print(f"Factorial of {num} is {ret}.")

if __name__ == "__main__":
    main()


