import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score, confusion_matrix

###########################################################################
# Step1: Load the data
###########################################################################

print("Marvellous wine cutivators case study")

border = "-"*50

print(border)
print("Step1: Load the data")
print(border)


df = pd.read_csv("WinePredictor.csv")

print("Data shape is : ", df.shape)

print("Data loaded successfully")

###########################################################################
# Step2: Clean, prepare and manipulate data
###########################################################################

print(border)
print("Step2: Clean, prepare and manipulate data")
print(border)

df.dropna(inplace=True)

print("Shape of dataset is : ", df.shape)

print("Total recors : ", df.shape[0])
print("Total columns : ", df.shape[1])
print(border)

###########################################################################
# Step3: Seprate independent and depenedent variables
###########################################################################

print(border)
print("Step3: Seprate independent and depenedent variables")
print(border)

X = df.drop(columns=["Class"])
Y = df["Class"]

print("Independent variables are : ", X.columns.to_list())
print("Dependent variable is : ", "Class")

print("X shape is : ", X.shape)
print("Y shape is : ", Y.shape)

###########################################################################
# Step4: Split the dataset for training and testing
###########################################################################

print(border)
print("Step4: Split the dataset for training and testing")
print(border)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.5, random_state = 42, stratify=Y)

print("X_train shape is : ", X_train.shape)
print("X_test shape is : ", X_test.shape)
print("Y_train shape is : ", Y_train.shape)
print("Y_test shape is : ", Y_test.shape)

print(border)

print(border)
print("Step 4.1 : Feature scaling")
print(border)

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.fit_transform(X_test)

###########################################################################
# Step5: Build the model
###########################################################################

print(border)
print("Step5: Build the model")
print(border)

#model = DecisionTreeClassifier(max_depth=9)
model = KNeighborsClassifier(n_neighbors=9)

print("Model build successfully")

print(border)

###########################################################################
# Step6: Train the model
###########################################################################

print(border)
print("Step6: Train the model")
print(border)

model = model.fit(X_train_scaled, Y_train)

print("Model trained successfully")

###########################################################################
# Step7: Evaluate the model
###########################################################################

print(border)
print("Step7: Evaluate the model")
print(border)

Y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_test, Y_pred)

print("Model accuracy is : " , accuracy*100)

cm = confusion_matrix(Y_test, Y_pred)
print("Confusion matrix is : ", cm)