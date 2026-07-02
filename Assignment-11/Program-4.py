def reverseNum(num):
    reverse = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        reverse = rem + (reverse * 10)

    print("Reverse is :", reverse)

def main():
    num = int(input("Enter a number:"))
    reverseNum(num)

if __name__ == "__main__":
    main()