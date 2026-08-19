import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

border = "-"*50

def loadDataSet(filename):
    df = pd.read_csv(filename)

    return df
    
def preProcessData(df):
    df = df.drop(columns=[df.columns[0]], axis=0)
    return df

def separateFeaturesAndLabels(df):
    X = df.drop(columns=["sales"])
    Y = df["sales"]

    return X, Y

def splitDataset(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    return X_train, X_test, Y_train, Y_test  

def trainModel(X_train, Y_train):
    model = LinearRegression()
    model = model.fit(X_train, Y_train)
    return model

def testModel(model, X_test):
    Y_pred = model.predict(X_test)
    return Y_pred

def main():
    # Step 1

    df = loadDataSet("Advertising.csv")

    print(border)
    print("Data loaded successfully")
    print("Dataset is : ")
    print(df)
    
    print(border)
    print("Dataset shape is : ")
    print(df.shape)
    print(border)

    # Step 2

    df = preProcessData(df)
    print("Dataset preprocessing is done")
    print("Total missing values : ")
    print(df.isnull().sum())
    print(border)
    print(df)
    print(border)

    print("Statistical report of dataset : ")
    print(df.describe())
    print(border)

    # Step 3
    X, Y = separateFeaturesAndLabels(df)

    print("Independent variables are : ")
    print(X.columns.tolist())
    print("X shape is : ", X.shape)
    print("Dependent variables are : ")
    print(Y.name)
    print("Y shpae is : ", Y.shape)
    print(border)

    # Step 4

    X_train, X_test, Y_train, Y_test = splitDataset(X, Y)
    print("Dataset splitted successfully")
    print("X_train shape : ", X_train.shape)
    print("Y_train shape: ", Y_train.shape)
    print("X_test shape : ", X_test.shape)
    print("Y_test shape: ", Y_test.shape)
    print(border)

    # Step 5

    model = trainModel(X_train, Y_train)
    print("Model trained successfully")
    print(border)

    # Step 6

    Y_pred = testModel(model, X_test)
    print("Model tested successfully")
    print(border)

    print("Actual and predicted values are: ")
    for i in range(len(Y_test)):
        print("Actual is: ", Y_test.values[i], " Predicted is : ", Y_pred[i])

    print(border)
    print("Assignment 46 is completed")
    print(border)
if __name__ == "__main__":
    main()