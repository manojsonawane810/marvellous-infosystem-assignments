import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
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
# Step2 : Data analysis (EDA)
#########################################################################

print(border)
print("Step2 : Data analysis (EDA)")
print(border)

print("Shape of dataset : ", df.shape)
print("Column names are : ", list(df.columns))
print("Class distribution FinalResult : ")
print(df["FinalResult"].value_counts())
print("Missing values per column: ")
print(df.isnull().sum())
print("Statistical report of dataset:")
print(df.describe())

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

#########################################################################
# Step3 : Visualization of dataset
#########################################################################

print(border)
print("Step3 : Visualization of dataset")
print(border)

plt.figure(figsize=(7,5))

for result in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == result]
    plt.scatter(temp["StudyHours"], temp["Attendance"], label=result)

plt.title("Student perforamance stats")
plt.xlabel("StudyHours")
plt.ylabel("Attendance")

plt.legend()
plt.grid()
plt.show()

#########################################################################
# Step4 : Split the datatset for training and testing
#########################################################################

print(border)
print("Step4 : Split the datatset for training and testing")
print(border)

X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size= 0.3, random_state=42)

print("X_train shape : ", X_train.shape)
print("Y_train shape : ", Y_train.shape)

print("X_test shape : ", X_test.shape)
print("Y_test shape : ", Y_test.shape)

print("Spliting of training and testing data is done")

#########################################################################
# Step5 : Train the model
#########################################################################

print(border)
print("Step5 : Train the model")
print(border)

model = DecisionTreeClassifier(max_depth=3)
print("Model built successfully")

model = model.fit(X_train, Y_train)
print("Model trained successfully")

#########################################################################
# Step6 : Evaluate the model
#########################################################################

print(border)
print("Step6 : Evaluate the model")
print(border)

Y_pred = model.predict(X_test)

print("Model evaluated successfully")

#########################################################################
# Step7 : Evaluate the model performance
#########################################################################

print(border)
print("Step7 : Evaluate the model performance")
print(border)

accuracy = accuracy_score(Y_test, Y_pred)
print("Model accuracy is : ", accuracy*100)

#########################################################################
# Step8 : Confusion matrix creation
#########################################################################

print(border)
print("Step8 : Confusion matrix creation")
print(border)

cm = confusion_matrix(Y_test, Y_pred)

print("Confusion matrix is : ")
print(cm)

#########################################################################
# Step9 : Final conclusion
#########################################################################

print(border)
print("Step9 : Final conclusion")
print(border)
      
Y_pred = model.predict(X_train)
trainAcc = accuracy_score(Y_train, Y_pred)

print("Training accuracy is : ", trainAcc*100)

print("Training accuracy is greater than testing accuracy.")

print("Assignment 39 Question number 8 is completed.")