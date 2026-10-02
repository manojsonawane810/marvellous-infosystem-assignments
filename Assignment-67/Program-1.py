import numpy as np
import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

def main():
    # Create dataset

    inputs = np.array([
        [25, 500, 12, 1, 2],
        [30, 700, 24, 0, 1],
        [45, 1200, 6, 5, 8],
        [50, 1500, 5, 6, 10],
        [28, 600, 18, 1, 1],
        [35, 800, 30, 0, 0],
        [48, 1400, 4, 7, 9],
        [52, 1600, 3, 8, 12],
        [27, 550, 20, 0, 1],
        [42, 1300, 8, 4, 7]
    ])

    output = [0, 0, 1, 1, 0, 0, 1, 1, 0, 1]

    X = pd.DataFrame(inputs, columns=["Age", "Monthly Charges", "Tenure", "Complaints", "Support Calls"])
    Y = pd.DataFrame(output, columns=["Leave"])

    print(X)
    print(Y)

    # Clean dataset, age is not be required, so lets drop it

    X = X.drop(columns=["Age"])
    print(X)

    # Apply standard scalling

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    print("Scaled dataset is : ")
    print(X_scaled)

    # Split dataset

    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.5, random_state=42)

    print("X_train shape: ", X_train.shape)
    print("X_test shape: ", X_test.shape)
    print("Y_train shape: ", Y_train.shape)
    print("Y_test shape: ", Y_test.shape)

    # Create FNN model

    model = MLPClassifier(
        hidden_layer_sizes=(5),
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    # Train the model

    model = model.fit(X_train, Y_train)

    # Evaluate model

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy of the model is : ", accuracy * 100)

    # Test new customer
    
    newTest = [[46, 150, 5, 6, 9]]

    newData = pd.DataFrame(newTest, columns=["Age", "Monthly Charges", "Tenure", "Complaints", "Support Calls"])
    newData = newData.drop(columns=["Age"])
    newScaledData = scaler.fit_transform(newData)

    result = model.predict(newScaledData)
    print("Result is : ", result)

    if (result == 1):
        print("Customer will leave")
    else:
        print("Customer will stay")
if __name__ == "__main__":
    main()