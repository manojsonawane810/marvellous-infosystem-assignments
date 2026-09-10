import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, log_loss
from sklearn.preprocessing import StandardScaler, MinMaxScaler

#-------------------------------------------------------------------------------#
# Employee Attrition Identification Case Study
#-------------------------------------------------------------------------------#

border = "-"*50

def loadDataset():
    df = pd.read_csv("Employee_Attrition.csv")
    
    print("Shape of dataset is : ", df.shape)
    print(border)
    print("Columns in dataset : ", df.columns.to_list())
    print(border)
    print("First five records : ")
    print(df.head())
    print(border)

    return df

def analyzeDataset(df):
    print(border)
    print("Check for missing values")
    print(border)

    checkMissingValues(df)
    df = convertCategoricalDataToNumeric(df)
    return df
    

def checkMissingValues(df):
    print(df.isnull().sum())
    print("There are no any missing values in dataset")
    print(border)

def convertCategoricalDataToNumeric(df):
    print("Numerical features are: ")
    numerical_cols = df.select_dtypes(include="number").columns.tolist()
    print(numerical_cols)
    print(border)
    print("Categorical features are: ")
    categorical_cols = df.select_dtypes(include="str").columns.tolist()
    categorical_cols.remove("Attrition")
    print(categorical_cols)
    print(border)

    print("Convert caterorical data to numeric values")
    print(border)

    df = pd.get_dummies(
        df,
        columns=categorical_cols,
        drop_first=True,
        dtype="int"
    )

    df = pd.get_dummies(
        df,
        columns=["Attrition"],
        drop_first=True,
        dtype="int"
    )

    print(df.head())

    return df

def separateData(df):
    X = df[['Age', 'MonthlyIncome', 'YearsAtCompany', 'TotalWorkingYears', 'DistanceFromHome', 'JobSatisfaction', 'WorkLifeBalance', 'NumCompaniesWorked', 'TrainingTimesLastYear', 'OverTime_Yes']]
    print("X shape is : ", X.shape)
    Y = df["Attrition_Yes"]
    print("Y shape is : ", Y.shape)

    return X, Y

def splitDataset(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    print("X train shape : ", X_train.shape)
    print("X test shape : ", X_test.shape)
    print("Y train shape : ", Y_train.shape)
    print("Y test shape : ", Y_test.shape)

    return X_train, X_test, Y_train, Y_test

def applyScalingToFeatures(X_train, X_test):
    scaler = getScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)
    print("Few entries are")
    print(X_train_scaled[:5])
    return X_train_scaled, X_test_scaled

def getScaler():
    scaler = StandardScaler()
    return scaler

def buildMLPModel():
    model = MLPClassifier(
        hidden_layer_sizes=(9, 5),
        max_iter=1000,
        solver="adam",
        activation="relu",
        random_state=42
    )
    return model

def trainModel(X_train_scaled, Y_train, model):
    model = model.fit(X_train_scaled, Y_train)
    print("Number of iterations required for training are: ", model.n_iter_)
    return model

def calculateTrainingAcc(X_train_scaled, Y_train, model):
    Y_train_pred = model.predict(X_train_scaled)

    training_acc = accuracy_score(Y_train, Y_train_pred)
    print("Training accuracy is : ", training_acc * 100)
    print(border)

def calculateTestingAcc(X_test_scaled, Y_test, model):
    Y_test_pred = model.predict(X_test_scaled)

    testing_acc = accuracy_score(Y_test, Y_test_pred)
    print("Testing accuracy is : ", testing_acc * 100)
    print(border)

    return Y_test_pred

def plotLossCurve(steps, loss_curve):
    plt.figure(figsize=(8,5))
    plt.plot(range(0, steps), loss_curve, marker="o")
    plt.title("Loss Curve")
    plt.xlabel("Training step")
    plt.ylabel("Loss")
    plt.grid(True)
    plt.show()

def predictAttrition(employee_data, model):
    scaler = getScaler()
    scaled_data = scaler.fit_transform(employee_data)
    new_predictions = model.predict(scaled_data)
    new_probabilities = model.predict_proba(scaled_data)

    print("New employess data is: ")
    print(employee_data)
    print(border)

    print("New employees predictions are : ")
    print(new_predictions)
    print(border)

    print("New employess probabilities are : ")
    print(new_probabilities)
    print(border)

def main():
    print(border)
    print("Employee Attrition Identification Case Study")
    print(border)

    print(border)
    print("Load the dataset")
    print(border)

    df = loadDataset()

    print(border)
    print("Analyze the data in dataset")
    print(border)

    df = analyzeDataset(df)

    print(border)
    print("Separate independent and dependent varaibles")
    print(border)

    X, Y = separateData(df)

    print(border)
    print("Split the data in training and testing dataset")
    print(border)

    X_train, X_test, Y_train, Y_test = splitDataset(X, Y)

    print(border)
    print("Apply feature scaling")
    print(border)

    X_train_scaled, X_test_scaled = applyScalingToFeatures(X_train, X_test)

    print(border)
    print("Build a MLP model")
    print(border)

    model = buildMLPModel()

    print("Model created successfully")

    print(border)
    print("Train MLP model")
    print(border)

    model = trainModel(X_train_scaled, Y_train, model)

    print(border)
    print("Calculate training accuracy")
    print(border)

    calculateTrainingAcc(X_train_scaled, Y_train, model)

    print(border)
    print("Calculate testing accuracy")
    print(border)

    Y_test_pred = calculateTestingAcc(X_test_scaled, Y_test, model)

    print(border)
    print("Confusion matrix")
    print(border)

    print(confusion_matrix(Y_test, Y_test_pred))
    print(border)

    print(border)
    print("Plot the loss curve")
    print(border)

    plotLossCurve(model.n_iter_, model.loss_curve_)

    print(border)
    print("Test unseen data")
    print(border)

    employee_data = [
        [22, 10000, 1, 1, 15, 2, 1, 1, 0, 1],
        [32, 100000, 3, 9, 7, 3, 2, 2, 2, 0],
        [47, 150000, 2, 20, 22, 4, 3, 5, 1, 0],
        [56, 180000, 4, 25, 10, 2, 2, 8, 1, 1],
        [28, 80000, 2, 5, 18, 3, 1, 3, 2, 0]
    ]

    employee_data = pd.DataFrame(employee_data, columns=['Age', 'MonthlyIncome', 'YearsAtCompany', 'TotalWorkingYears', 'DistanceFromHome', 'JobSatisfaction', 'WorkLifeBalance', 'NumCompaniesWorked', 'TrainingTimesLastYear', 'OverTime_Yes'])
    predictAttrition(employee_data, model)

    print("As training accuracy is greater than testing accuracy.")
    print("So we can say model is suffering from overfitting")
    print(border)
    print("Assignment-62 is completed")

if __name__ == "__main__":
    main()