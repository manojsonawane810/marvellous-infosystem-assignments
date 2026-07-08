import threading

def Small(value):
    print("DisplaySmall thread ID is: ", threading.get_ident() , " and thread name is: ", threading.current_thread().name)
    count = 0
    result = []
    
    for i in range(len(value)):
        if value[i].islower():
            count = count + 1
            result.append(value[i])
    
    print("Lowercase characters: ", result)
    print("Total lowercase characters are: ", count)

def Capital(value):
    print("DisplayCapital thread ID is: ", threading.get_ident() , " and thread name is: ", threading.current_thread().name)
    count = 0
    result = []
    
    for i in range(len(value)):
        if value[i].isupper():
            count = count + 1
            result.append(value[i])
    
    print("Uppercase characters: ", result)
    print("Total uppercase characters are: ", count)

def Digits(value):
    print("DisplayDigits thread ID is: ", threading.get_ident() , " and thread name is: ", threading.current_thread().name)
    count = 0
    result = []
    
    for i in range(len(value)):
        if value[i].isdigit():
            count = count + 1
            result.append(value[i])
    
    print("Digits characters: ", result)
    print("Total digits characters are: ", count)

def main():
    print("Main thread ID is: ", threading.get_ident() , " and thread name is: ", threading.current_thread().name)
    
    displaySmall = threading.Thread(target=Small, args=("1-June-2026",))
    displayCapital = threading.Thread(target=Capital, args=("30-July-2026",))
    displayDigits = threading.Thread(target=Digits, args=("31-Agust-2026",))
    
    displaySmall.start()
    displayCapital.start()
    displayDigits.start()

if __name__ == "__main__":
    main()