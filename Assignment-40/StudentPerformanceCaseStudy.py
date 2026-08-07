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

#########################################################################
# Step3 : Decide independent and dependent variables
#########################################################################

print(border)
print("Step3 : Decide independent and dependent variables")
print(border)

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
# Step4 : Visualization of dataset
#########################################################################

print(border)
print("Step4 : Visualization of dataset")
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
# Step5 : Split the datatset for training and testing
#########################################################################

print(border)
print("Step5 : Split the datatset for training and testing")
print(border)

X_train,X_test,Y_train,Y_test = train_test_split(X, Y, test_size= 0.3, random_state=42)

print("X_train shape : ", X_train.shape)
print("Y_train shape : ", Y_train.shape)

print("X_test shape : ", X_test.shape)
print("Y_test shape : ", Y_test.shape)

print("Spliting of training and testing data is done")

#########################################################################
# Step6 : Build the model
#########################################################################

print(border)
print("Step6 : Build the model")
print(border)


model = DecisionTreeClassifier(max_depth=3)
print("Model built successfully")

#########################################################################
# Step7 : Train the model
#########################################################################

print(border)
print("Step7 : Train the model")
print(border)

model = model.fit(X_train, Y_train)
print("Model trained successfully")

#########################################################################
# Step8 : Evaluate the model
#########################################################################

print(border)
print("Step8 : Evaluate the model")
print(border)

Y_pred = model.predict(X_test)

print("Model evaluated successfully")

#########################################################################
# Step9 : Evaluate the model performance
#########################################################################

print(border)
print("Step9 : Evaluate the model performance")
print(border)

accuracy = accuracy_score(Y_test, Y_pred)
print("Model accuracy is : ", accuracy*100)

#########################################################################
# Assignment Question 1 implmentation
#########################################################################

print(border)
print("Assignment Question 1 implmentation")
print(border)

impScore = model.feature_importances_

for i in range(len(impScore)):
    print(f"Important score of feature {df.columns[i]} is {impScore[i]}")

print("By looking at important score of the features it shows that StudyHours is contributing more in getting the final result")
print("However if we change the test-size parameter it may change")
print("Rest all other features like (Attendance,PreviousScore,AssignmentsCompleted,SleepHours) are not contributing or least contributing in getting the final result correctly")

#########################################################################
# Assignment Question 2 implmentation
#########################################################################

print(border)
print("Assignment Question 2 implmentation")
print(border)

feature_columns = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted"
]

X = df[feature_columns]
Y = df["FinalResult"]
df.pop("SleepHours")

print("X shape after removing the SleepHours : ", X.shape)
print("Column names: ", list(df.columns))

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

print("Dataset splitted after removing one feature")

model = DecisionTreeClassifier()
model = model.fit(X_train, Y_train)

print("Model has been trained again")

Y_pred = model.predict(X_test)

accuracyNew = accuracy_score(Y_test, Y_pred)

print("Accuracy after removing SleepHours : ", accuracyNew*100)

if accuracy < accuracyNew:
    print("Previous accuracy is less than new accuracy")
elif accuracy > accuracyNew:
    print("Previous accuracy is greather than new accuracy")
else:
    print("Previous accuracy is equal to new accuracy")
    print("Hence, removing SleepHours feature does not affect the performance")


#########################################################################
# Assignment Question 3 implmentation
#########################################################################

print(border)
print("Assignment Question 3 implmentation")
print(border)


feature_columns = [
    "StudyHours",
    "Attendance"
]

X = df[feature_columns]
Y = df["FinalResult"]
df.pop("PreviousScore")
df.pop("AssignmentsCompleted")

print("X shape with features StudyHours and Attendance : ", X.shape)
print("Column names: ", list(df.columns))

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

print("Dataset splitted again after removing the feature")

model = DecisionTreeClassifier()
model = model.fit(X_train, Y_train)

print("Model has been trained again")

Y_pred = model.predict(X_test)

accuracyNew = accuracy_score(Y_test, Y_pred)

print("Accuracy with features StudyHours and Attendance is: ", accuracyNew*100)

if accuracy < accuracyNew:
    print("Full feature model accuracy is less than new accuracy")
elif accuracy > accuracyNew:
    print("Full feature model accuracy is greather than new accuracy")
else:
    print("Full feature model accuracy is equal to new accuracy")
    print("Hence, removing SleepHours, PreviousScore and AssignmentsCompleted features does not affect the performance")
    print("Model is still performing well")

#########################################################################
# Assignment Question 4 implmentation
#########################################################################

print(border)
print("Assignment Question 4 implmentation")
print(border)

newDf = [[5, 88],[4.7, 78],[8, 66],[6.5, 91],[5.8, 80]]

newPred = model.predict(newDf)

for result in newPred:
    if result == 1:
        print("Prediction of new student is pass")
    else:
        print("Prediction of new student is fail")

#########################################################################
# Assignment Question 5 implmentation
#########################################################################

print(border)
print("Assignment Question 5 implmentation")
print(border)

print("Evaluating the model again to calculate the accuracy manually")
Y_pred = model.predict(X_test)

cm = confusion_matrix(Y_test, Y_pred)

TN, FP, FN, TP = cm.ravel()

accuracyManual = (TP + TN) / (TP+TN+FP+FN)
print("Manually calcuated accuracy is : ", accuracyManual*100)
if accuracy == accuracyManual:
    print("Sklearn accuracy is matching with manually calculated accuracy")

#########################################################################
# Assignment Question 6 implmentation
#########################################################################

print(border)
print("Assignment Question 6 implmentation")
print(border)

locationOfFailed = Y_test != Y_pred
y_test_mismatches = Y_test.loc[locationOfFailed]

misMatchedIndexes = y_test_mismatches.index.tolist()

for index in misMatchedIndexes:
    print("Mismatched row : ", df.loc[index])

print(f"Total {len(misMatchedIndexes)} students were mis classified")

#########################################################################
# Assignment Question 7 implmentation
#########################################################################

print(border)
print("Assignment Question 7 implmentation")
print(border)

print("Loading the dataset again to consider all features")

df = pd.read_csv(datasetFile)

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
print("Columns are: ", list(df.columns))

print("Training the model using random_state=0")
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
print("Model splitted successfully")

model = model.fit(X_train, Y_train)
print("Model trained successfully")

print("Predict the model")
Y_pred = model.predict(X_test)

accuracy1 = accuracy_score(Y_test, Y_pred)
print("Accuracy with random state 0 is : ", accuracy1*100)

print("Training the model using random_state=10")
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=10)
print("Model splitted successfully")

model = model.fit(X_train, Y_train)
print("Model trained successfully")

print("Predict the model")
Y_pred = model.predict(X_test)

accuracy2 = accuracy_score(Y_test, Y_pred)
print("Accuracy with random state 10 is : ", accuracy2*100)


print("Training the model using random_state=42")
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
print("Model splitted successfully")
model = DecisionTreeClassifier()
model = model.fit(X_train, Y_train)
print("Model trained successfully")

print("Predict the model")
Y_pred = model.predict(X_test)

accuracy3 = accuracy_score(Y_test, Y_pred)
print("Accuracy with random state 42 is : ", accuracy3*100)

print("Accuracy with random state 0 is 100 %")
print("Accuracy with random sate 10 and 42 is same that is 88.8888888")

#########################################################################
# Assignment Question 8 implmentation
#########################################################################

print(border)
print("Assignment Question 8 implmentation")
print(border)
print("Visualizing the trained decision tree")
plt.figure(figsize=(6,6))
pltTree = plot_tree(model)
plt.show()

print("Plot tree graph displayed.")
print("By looking at plot tree, X[1] which is second feature (Attendence) is the root node")
print("Attendece is selected as root node because, it is the main feature which decide the pattern flow till the last node and gives better performance")

#########################################################################
# Assignment Question 9 implmentation
#########################################################################

print(border)
print("Assignment Question 9 implmentation")
print(border)

print("Add PerformanceIndex feature in the dataframe")
#df["PerformanceIndex"] = df["StudyHours"]*2 + df["Attendance"]
df.insert(5, "PerformanceIndex", df["StudyHours"]*2 + df["Attendance"])
print("Datafram columns are : ", list(df.columns))

feature_columns.append("PerformanceIndex")
print("Independent variables are : ", feature_columns)

X = df[feature_columns]
Y = df["FinalResult"]

print("X shape : ", X.shape)
print("Y shape : ", Y.shape)
print("First 5 records of dataframe are : ")
print(X.head)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

model = DecisionTreeClassifier()

model = model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy of model is : ", accuracy*100)

print("Accuracy is same with PerformanceIndex feature. No change!")

#########################################################################
# Assignment Question 10 implmentation
#########################################################################

print(border)
print("Assignment Question 10 implmentation")
print(border)

print("Train model with max_depth=None")

model = DecisionTreeClassifier(max_depth=None)

model = model.fit(X_train, Y_train)

Y_pred = model.predict(X_train)

trainAcc = accuracy_score(Y_train, Y_pred)

print("Training accuracy is : ", trainAcc*100)

Y_pred = model.predict(X_test)

testAcc = accuracy_score(Y_test, Y_pred)

print("Testing accuracy is : ", testAcc*100)

print("Training accuracy is greater than testing accuracy due to higher percentage of training samples with multiple dataset and patterns")

print(border)
print("Assignment 40 is completed!")
print(border)

