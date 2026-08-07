import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

border = "-"*50

#########################################################################
# Step1 : Load the dataset
#########################################################################

print(border)
print("Step1 : Load the dataset")
print(border)

datasetFile = "student_performance_ml.csv"

df = pd.read_csv(datasetFile)

print("Dataset loaded successfully")

#########################################################################
# Assignment Question 1 implmentation
#########################################################################

print(border)
print("Assignment Question 1 implmentation")
print(border)

print("Shape of dataset : ", df.shape)
print("Column names are : ", list(df.columns))
print("Class distribution FinalResult : ")
print(df["FinalResult"].value_counts())
print("Missing values per column: ")
print(df.isnull().sum())

print("Data analysis is completed")

feature_columns = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_columns]
Y = df["FinalResult"]

print("X shape : ", X.shape)
print("Y shape : ", Y.shape)

print("Independent and dependent variables are identified.")

X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size= 0.2, random_state=42)

print("X_train shape : ", X_train.shape)
print("Y_train shape : ", Y_train.shape)

print("X_test shape : ", X_test.shape)
print("Y_test shape : ", Y_test.shape )

print("Spliting of training and testing data is done")

model = DecisionTreeClassifier()
model = model.fit(X_train, Y_train)

print("Model trained successfully")

#########################################################################
# Assignment Question 2 implmentation
#########################################################################

print(border)
print("Assignment Question 2 implmentation")
print(border)

Y_pred = model.predict(X_test)

print("Predicted values are : ", Y_pred)
print("Actual values are : ", list(Y_test))
print("Model evaluation is done")

#########################################################################
# Assignment Question 3 implmentation
#########################################################################

print(border)
print("Assignment Question 3 implmentation")
print(border)

accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy of the model is : ", accuracy*100)

#########################################################################
# Assignment Question 4 implmentation
#########################################################################

print(border)
print("Assignment Question 4 implmentation")
print(border)

cMarix = confusion_matrix(Y_test, Y_pred)

print("Confusion matrix is : ")
print(cMarix)

print(border)
print("As per confusion matrix, consider fail is positive, so pass is negative")
print("True Positive: actual = fail, predicted = fail. There are total 5 match of true positive")
print("True positive = 5")
print(border)

print("True Negative: actual = pass, predicted = pass. There are total 1 match of true negative")
print("True negative = 1")
print(border)

print("False positive: actual = pass, predicted = fail. There are no match of false positive")
print("False positive = 0")
print(border)

print("False negative: actual = fail, predicted = pass. There are no match of false negative")
print("False negative = 0")
print(border)


#########################################################################
# Assignment Question 5 implmentation
#########################################################################

print(border)
print("Assignment Question 5 implmentation")
print(border)

trainPred = model.predict(X_train)

trainingAccu = accuracy_score(Y_train, trainPred)
print("Training accuracy is : ", trainingAccu*100)
print("Testing accuracy is : ", accuracy*100)

print("Training accuracy is exactly same with testing accuracy.")
print("Model is not overfitting or underfitting.")

#########################################################################
# Assignment Question 6 implmentation
#########################################################################

print(border)
print("Assignment Question 6 implmentation")
print(border)

model1 = DecisionTreeClassifier(max_depth=1)
model2 = DecisionTreeClassifier(max_depth=3)
model3 = DecisionTreeClassifier(max_depth=None)

model1 = model1.fit(X_train, Y_train)
model1Pred = model1.predict(X_test)

model1Acc = accuracy_score(Y_test, model1Pred)
print("Accuracy of model 1 with max_depth=1 is : ", model1Acc*100)

model2 = model2.fit(X_train, Y_train)
model2Pred = model2.predict(X_test)

model2Acc = accuracy_score(Y_test, model2Pred)
print("Accuracy of model 2 with max_depth=3 is : ", model2Acc*100)

model3 = model3.fit(X_train, Y_train)
model3Pred = model3.predict(X_test)

model3Acc = accuracy_score(Y_test, model3Pred)
print("Accuracy of model 3 with max_depth=None is : ", model3Acc*100)

print("Accuracy of Model 1, Model 2 and Model 3 is same with different max depth value. ")

#########################################################################
# Assignment Question 7 implmentation
#########################################################################

print(border)
print("Assignment Question 7 implmentation")
print(border)

model = DecisionTreeClassifier(max_depth=5)
model = model.fit(X_train, Y_train)

studentPred = model.predict([[6, 85, 66, 7, 7]])
if studentPred == 1:
    print("Student is paased")
else:
    print("Student is failed")


#########################################################################
# Assignment Question 8 implmentation
#########################################################################

print(border)
print("Assignment Question 8 implmented in another file. Please run it.")
print(border)

print("Assignment 39 is completed")
