import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

def main():
    X = [
        [25000, 600, 200000, 10000, 0],
        [40000, 700, 300000, 8000, 1],
        [60000, 750, 500000, 12000, 1],
        [20000, 550, 150000, 15000, 0],
        [80000, 800, 700000, 10000, 1],
        [35000, 650, 250000, 9000, 1],
        [18000, 500, 100000, 12000, 0],
        [90000, 850, 800000, 15000, 1],
        [30000, 580, 200000, 14000, 0],
        [70000, 780, 600000, 10000, 1]
    ]

    data = pd.DataFrame(X, columns=["Income", "Credit Score", "Loan Amount", "Existing EMI", "Employment Status"])

    print("Data is : ")
    print(data.head())
    print("Shape of dataset is : ", data.shape)

    # seperate features and labels

    X = data.drop(columns=["Employment Status"])
    Y = data["Employment Status"]

    print("X data is :")
    print(X.head())
    print("X shape is: ", X.shape)
    print("Y shape is: ", Y.shape)

    # Apply scaling

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split data

    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.5, random_state=42)

    print("X train shape: ", X_train.shape)
    print("Y train shape: ", Y_train.shape)

    print("X test shape: ", X_test.shape)
    print("Y test shape: ", Y_test.shape)

    # create and Train model

    model = MLPClassifier(
        hidden_layer_sizes=(4,),
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    model = model.fit(X_train, Y_train)
    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy of model is : ", accuracy * 100)

    newData = [[55000, 720, 400000, 10000]]
    data = pd.DataFrame(newData, columns=["Income", "Credit Score", "Loan Amount", "Existing EMI"])

    data = scaler.fit_transform(data)

    result = model.predict(data)

    if result == 1:
        print("Stable")
        print("Loan will be approved")
    else:
        print("Not Stable")
        print("Loan will be rejected")
    
if __name__ == "__main__":
    main()