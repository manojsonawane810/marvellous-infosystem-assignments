def isDivisibleBy(num):
    if num % 5 == 0:
        return True
    else:
        return False

def main():
    num = int(input("Enter a number: "))
    ret = isDivisibleBy(num)

    if(ret):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()