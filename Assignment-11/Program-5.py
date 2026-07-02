def reverseNum(num):
    reverse = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        reverse = rem + reverse * 10
    
    return reverse

def checkPalindrome(num):
    reverseNo = reverseNum(num)

    if num == reverseNo:
        print(num, " is a palindrome number")
    else:
        print(num, " is not a palindrome number")

def main():
    num = int(input("ENter a number:"))

    checkPalindrome(num)

if __name__ == "__main__":
    main()
