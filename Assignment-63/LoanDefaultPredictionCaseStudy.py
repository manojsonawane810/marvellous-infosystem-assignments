#-----------------------------------------------------------------------------#
#   Loan Default Prediction Case Study
#-----------------------------------------------------------------------------#

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler

border = "-"*50
def loadDataset():
    df = pd.read_csv("Loan_Default.csv")
    print(border)
    print("Dataset loaded successfully")
    print("First few records are: ")
    print(df.head())
    print(border)
    return df

def performEDA(df):
    print("Shape of dataset is : ", df.shape)
    print(border)

    print("Dataset overall values are : ")
    print(df.describe())
    print(border)
        
    print("Check for any missing values: ")
    print(df.isnull().sum())
    print("There are no any missing values in columns.")
    print(border)

    print("Check if any duplicate data is available: ")
    print(df.duplicated().sum())
    print(border)

def checkTargetClassImbalance(df):
    print(df["Default"].value_counts(normalize=True))
    print(border)
    targetClassCounts = df["Default"].value_counts()

    imbalance_ratio = targetClassCounts.max() / targetClassCounts.min()

    if imbalance_ratio > 2:
        print("Target classes are imbalanced, ratio is : ", imbalance_ratio)
    else:
        print("Target classes are balanced")
    print(border)
   

def checkCategoricalCol(df):
    categoricalCols = df.select_dtypes(include="str").columns.tolist()
    print("Categorical columns are: ")
    print(categoricalCols)
    print(border)
    return categoricalCols

def encodeCategoricalVar(df, categoricalCols):
    df = pd.get_dummies(
        df,
        columns=categoricalCols,
        drop_first=True,
        dtype="int"
    )
    print("Data has been encoded. The first 5 entries are: ")
    print(border)
    print(df.head())
    
    return df

def separateVariables(df):
    X = df.drop(columns=["Default"])
    Y = df["Default"]

    print("X idependent shape is : ", X.shape)
    print("Y dependent shape is : ", Y.shape)
    print(border)
    print("First few feature records:")
    print(X[:5])
    return X, Y
def splitDataset(X, Y):
    
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )
    print("Target clasess percentage distribution before stratifying dataset")
    print(border)
    print("Training classes distribution: ", Y_train.value_counts(normalize=True) * 100)
    print("Testing classes distribution: ", Y_test.value_counts(normalize=True) * 100)
    print(border)

    print("As dataaset is having imbalanced target classes, we have to maintain the balanced percentage of each class. ")
    print("To have the balanced data in both training and testing dataset, we need to stratify the target data.")
    print(border)

    print("Target clasess percentage distribution after stratifying dataset")
    print(border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42, stratify=Y
    )

    print("Training classes distribution: ", Y_train.value_counts(normalize=True) * 100)
    print("Testing classes distribution: ", Y_test.value_counts(normalize=True) * 100)

    return X_train, X_test, Y_train, Y_test

def getScaler():
    scaler = StandardScaler()
    return scaler

def scaleFeatures(X_train, X_test):
    scaler = getScaler()
    x_train_scaled = scaler.fit_transform(X_train)
    x_test_scaled = scaler.fit_transform(X_test)

    print("Feature scaling is done.")
    print(border)
    print("Few records are : ")
    print(x_train_scaled[:5])

    return x_train_scaled, x_test_scaled

def buildModel():
    model = MLPClassifier(
        hidden_layer_sizes=(100, 50, 25),
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    print("MLP model is created")
    return model

def trainModel(X_train_scaled, Y_train, model):
    model = model.fit(X_train_scaled, Y_train)
    print("Model trained successfully.")
    return model

def predictModel(x_test_scaled, model):
    Y_pred = model.predict(x_test_scaled)
    print("Model testing is done")
    return Y_pred

def calculateAccuracy(Y_test, Y_pred):
    accuracy = accuracy_score(Y_test, Y_pred)
    print("Accuracy of the model is : ", accuracy * 100)

def calConfusionMatrix(Y_test, Y_pred):
    print("Confusion matrix is: ")
    print(confusion_matrix(Y_test, Y_pred))

def generateClassificationReport(Y_test, Y_pred):
    print("Classification report is : ")
    print(classification_report(Y_test, Y_pred))

def calPrecision(Y_test, Y_pred):
    print("Precision score is:")
    print(precision_score(Y_test, Y_pred))

def calRecall(Y_test, Y_pred):
    print("Recall score is:")
    print(recall_score(Y_test, Y_pred))

def calF1Score(Y_test, Y_pred):
    print("F1 score is:")
    print(f1_score(Y_test, Y_pred))

def plotTrainingLoss(loss):
    print("Plot the training loss")
    plt.figure(figsize=(8,6))
    plt.plot(loss, label="Training loss")
    plt.title("Training Loss Plot")
    plt.xlabel("Training steps")
    plt.ylabel("Loss")
    plt.grid(True)
    plt.legend()
    plt.show()

def predictNewApplicants(model, new_applicants):
    print("Predict the result of new applicants")
    scaler = getScaler()
    new_applicants_scaled = scaler.fit_transform(new_applicants)

    Y_pred_new = model.predict(new_applicants_scaled)
    print(border)
    print("New data is : ")
    print(new_applicants)

    print(border)
    print("Predicted results are:")
    print(Y_pred_new)




def main():
    print(border)
    print("Loan Default Prediction Case Study")
    print(border)

    print("Load the dataset")
    print(border)
    df = loadDataset()

    print(border)
    print("Perform exploratory data analysis")
    print(border)
    performEDA(df)

    print(border)
    print("Check if target classes are imbalanced: ")
    print(border)
    checkTargetClassImbalance(df)

    print(border)
    print("Identify categorical columns:")
    print(border)
    categoricalCols = checkCategoricalCol(df)

    print(border)
    print("Encode categorical variables:")
    print(border)
    df = encodeCategoricalVar(df, categoricalCols)

    print(border)
    print("Separate independent and dependent variables:")
    print(border)

    X, Y = separateVariables(df)

    print(border)
    print("Split the dataset into training and testing data.")
    print(border)

    X_train, X_test, Y_train, Y_test = splitDataset(X, Y)

    print(border)
    print("Scale the features")
    print(border)

    x_train_scaled, x_test_scaled= scaleFeatures(X_train, X_test)

    print(border)
    print("Create the MLP model")
    print(border)

    model = buildModel()
    print(border)

    model = trainModel(x_train_scaled, Y_train, model)
    print(border)

    Y_pred = predictModel(x_test_scaled, model)
    print(border)

    calculateAccuracy(Y_test, Y_pred)
    print(border)

    calConfusionMatrix(Y_test, Y_pred)
    print(border)

    generateClassificationReport(Y_test, Y_pred)
    print(border)

    calPrecision(Y_test, Y_pred)
    print(border)

    calRecall(Y_test, Y_pred)
    print(border)

    calF1Score(Y_test, Y_pred)
    print(border)

    plotTrainingLoss(model.loss_curve_)
    print(border)

    new_applicants = [
        [55, 641000, 345000, 677, 2, 1, 10000, 10, 0, 1, 0],
        [35, 541000, 234789, 546, 5, 3, 22000, 5, 1, 0, 1],
        [75, 741000, 120987, 785, 0, 0, 20000, 0, 0, 1, 0],
        [26, 841000, 564003, 456, 3, 2, 12000, 8, 0, 0, 1] 
    ]

    new_applicants = pd.DataFrame(new_applicants, columns=['Age', "Income", "LoanAmount", "CreditScore", "EmploymentYears", "ExistingLoans", "MonthlyDebt", "LoanTerm", "PreviousDefault_Yes", "HomeOwnership_Own", "HomeOwnership_Rent"])

    predictNewApplicants(model, new_applicants)

    print(border)

    print("HyperParameter experiment is done. ")
    print(border)
    print("Assignment-63 is completed!")



if __name__ == "__main__":
    main()