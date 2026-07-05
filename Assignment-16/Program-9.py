def getFirst10EvenNumbers():
    countOfResult = 10
    
    for no in range(1, 100):
        if no % 2 == 0:
            print(no)
            countOfResult = countOfResult - 1
        if countOfResult == 0:
            break
            
def main():
    getFirst10EvenNumbers()

if __name__ == "__main__":
    main()