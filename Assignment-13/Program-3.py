def checkPerfectNum(num):
    if num % 2 == 0:
        div = num // 2
        sum = 0
        print("div is ", div) 
        for i in range(1, div + 1):
            if num % i == 0:
                sum = sum + i

        if num == sum:
            print(num, " is a perfect number")
        else:
            print(num, " is not a perfect number")
    else:
        print(num, " is not a perfect number")

def main():
    num = int(input("Enter a number: "))

    checkPerfectNum(num)

if __name__ == "__main__":
    main()