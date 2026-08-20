from sklearn.metrics import classification_report

def main():
    border = "-"*50

    actual = [1, 1, 1, 1, 0, 0, 0, 0]
    predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    report = classification_report(actual, predicted)

    print(border)
    print("Classification report of data is : ")
    print(report)
    print(border)
    

if __name__ == "__main__":
    main()