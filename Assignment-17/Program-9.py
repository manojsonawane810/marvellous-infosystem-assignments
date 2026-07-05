def countDigits(num):
    count = 0
    while num > 0:
        num = num // 10
        count = count + 1
        
    return count

def main():
    num = int(input("Enter a number: "))
    count = countDigits(num)
    print("Digits in number is: ", count)

    textNum = input("Enter a number: ")
    print("Count of textNum is: ", len(textNum))

if __name__ == "__main__":
    main()