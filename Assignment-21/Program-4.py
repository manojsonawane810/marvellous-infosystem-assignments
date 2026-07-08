import threading

sum = 0
multi = 1

def calculateSum(numbers):
    global sum
    for no in numbers:
        sum = sum + no

def calculateProduct(numbers):
    global multi
    for no in numbers:
        multi = multi * no

def main():
    numbers = [10, 20, 45, 66, 33, 76, 89, 100, 43, 22, 21, 4, 8, 97, 10]

    addition = threading.Thread(target=calculateSum, args=(numbers,), name="addThread")
    product = threading.Thread(target=calculateProduct, args=(numbers,), name="productThread")

    addition.start()
    product.start()

    addition.join()
    product.join()

    print("Addition of numbers is : ", sum)
    print("Multiplication of numbers is : ", multi)

    print("Exit from main")

if __name__ == "__main__":
    main()