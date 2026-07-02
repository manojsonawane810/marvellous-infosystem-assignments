def countDigits(num):
    count = 0
    if num == 0:
        count = count + 1

    while num > 0:
        num = num // 10
        count = count + 1
     
    print("Digits count is :", count)

def main():
    num = 0
    num = int(input("Enter a number: "))
    countDigits(num)

if __name__ == "__main__":
    main()