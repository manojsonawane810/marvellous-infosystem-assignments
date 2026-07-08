import threading

orderNumber = 0

def addOrder():
    print(f"{threading.current_thread().name} is being processed.")
    global orderNumber
    orderNumber = orderNumber + 1
        
def processMealOrders():
    orderNumber = 0
    print(f"{threading.current_thread().name} ID is: {threading.get_ident()}")
    for i in range(1, 1000, 1):
        addOrder()  
        orderNumber = orderNumber + 1
    print(f"Total meal orders processed are: {orderNumber}")

def processBreakFastOrders():
    orderNumber = 0
    print(f"{threading.current_thread().name} ID is: {threading.get_ident()}")
    for i in range(1, 2000, 1):
        addOrder()  
        orderNumber = orderNumber + 1
    print(f"Total breakfast orders processed are: {orderNumber}")

def processFastFoodOrders():
    orderNumber = 0
    print(f"{threading.current_thread().name} ID is: {threading.get_ident()}")
    for i in range(1, 3000, 1):
        addOrder()    
        orderNumber = orderNumber + 1
    print(f"Total fastfood orders processed are: {orderNumber}")

def processDinnerOrders():
    orderNumber = 0
    print(f"{threading.current_thread().name} ID is: {threading.get_ident()}")
    for i in range(1, 700, 1):
        addOrder()  
        orderNumber = orderNumber + 1
    print(f"Total dinner orders processed are: {orderNumber}")


def main():
    print(f"{threading.current_thread().name} ID is: {threading.get_ident()}")
    

    thread1 = threading.Thread(target=processMealOrders, name="Meal-Thread")
    thread2 = threading.Thread(target=processBreakFastOrders, name="Breakfast-Thread")
    thread3 = threading.Thread(target=processFastFoodOrders, name="FastFood-Thread")
    thread4 = threading.Thread(target=processDinnerOrders, name="Dinner-Thread")

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    print("Total orders processed are: ", orderNumber)
    print("Exit from main")

if __name__ == "__main__":
    main()