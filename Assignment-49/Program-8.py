from sklearn.metrics import confusion_matrix

def main():
    actual = [1, 1, 1, 1, 0, 0, 0, 0]
    predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    cm = confusion_matrix(actual, predicted)

    print("Confusion matrix is: ")
    print(cm)
    print("-"*50)

    TN, FP, FN, TP = cm.ravel()

    print(f"TN : {TN}, FP: {FP}, FN: {FN}, TP: {TP}")

if __name__ == "__main__":
    main()