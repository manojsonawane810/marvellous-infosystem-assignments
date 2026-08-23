import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    border = "-"*50

    print(border)
    print("Breast cancer case study")
    print(border)

    # Step 1: Load the dataset

    print(border)
    print("Step 1: Load the dataset")
    print(border)

    dataset = load_breast_cancer()
    print(dataset)
    df = pd.DataFrame(dataset.data)
    print("Dataset loaded successfully. Shape is : ", df.shape)
    print("Few entries from dataset are:")
    print(df.head())
    print(border)

    print("Dataset info:")
    print(df.info())
    print(border)

    print(border)
    print("Feature names : ")
    print(dataset.feature_names)
    print(border)

    print("Target names: ")
    print(dataset.target_names)

    # Step 2: Preprocess the dataset
    
    print(border)
    print("Step 2: Preprocess the dataset")
    print(border)

    print("Total missing values: ")
    print(border)
    print(df.isnull().sum())
    print(border)

    print("Check for duplicate rows")
    print(border)
    print(df.duplicated().sum())
    print(border)

    print("Statistical Summary: ")
    print(border)
    print(df.describe())
    print(border)


    print("Features correlation: ")
    print(border)
    corr = df.corr()
    print(corr)
    print(border)

    print("Visualize the correlations of features: ")
    print(border)

    plt.figure(figsize=(10,10))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.show()

    # Step 3 : Split the dataset

    print(border)
    print("Step 3 : Split the dataset")
    print(border)

    print("Seperating independent and dependent variables: ")
    print(border)

    X = dataset.data
    print("X shape is : ", X.shape)

    Y = dataset.target
    print("Y shape is : ", Y.shape)
    print(border)

    print("Normalize or Scale the features ")
    print(border)
        
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
        
    print("Scaled data: ")
    print(X_scaled)
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

    print("X train shape : ", X_train.shape)
    print("Y train shape : ", Y_train.shape)
    print("X test shape : ", X_test.shape)
    print("Y test shape : ", Y_test.shape)
    print(border)

    # Step 4: Train the model

    print(border)
    print("Step 4: Train the model")
    print(border)

    model = LogisticRegression(max_iter=1000)

    model = model.fit(X_train, Y_train)

    print("Model trained successfully")
    print(border)

    # Step 5 : Test the model

    print(border)
    print("Step 5 : Test the model")
    print(border)

    Y_pred = model.predict(X_test)

    print("Model testing completed")

    # Step 6 : Evaluate the model

    print(border)
    print("Step 6 : Evaluate the model")
    print(border)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Testing accuracy is : ", accuracy * 100)
    print(border)

    trainPred = model.predict(X_train)

    trainAcc = accuracy_score(trainPred, Y_train)
    print("Training accuracy is : ", trainAcc * 100)
    print(border)
    

    print("Classification report : ")
    print(classification_report(Y_test, Y_pred))
    print(border)

    print("Confusion matrix : ")
    print(confusion_matrix(Y_test, Y_pred))
    print(border)

    print("Training and testing accuracies are closer to each other.")
    print("This means that model is best fitting")
    
    print(border)
    print("Assignment 50 completed")
    print(border)
    

if __name__ == "__main__":
    main()