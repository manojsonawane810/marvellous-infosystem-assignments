import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, classification_report

def buildVotingModel(voteType):
    model_tree = buildDetModel()
    model_logi = buildLogisModel()
    model_knn = buildKnnModel()

    model = VotingClassifier(
        estimators=[
            ("logistic", model_logi),
            ("decision_tree", model_tree),
            ("knn", model_knn)
        ],
        voting=voteType
    )
    return model

def buildLogisModel():
    model_logi = LogisticRegression(
        max_iter=1000, random_state=42
    )

    return model_logi

def buildKnnModel():
    model_knn = KNeighborsClassifier(
        n_neighbors=7,
    )
    return model_knn
    
def buildDetModel():
    model_tree = DecisionTreeClassifier(
        max_depth=7,
        random_state=42
    )
    return model_tree        

def calculateAccuracy(model, X_test, Y_test):
    Y_pred = model.predict(X_test)
    accuracy = accuracy_score(Y_test, Y_pred)

    return accuracy * 100

def trainKNN(X_train, Y_train):
    model_knn = buildKnnModel()
    return model_knn.fit(X_train, Y_train)

def trainDecisionTree(X_train, Y_train):
    model_tree = buildDetModel()
    return model_tree.fit(X_train, Y_train)

def trainLogistics(X_train, Y_train):
    model_logi = buildLogisModel()
    
    return model_logi.fit(X_train, Y_train)

def splitDataset(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    return X_train, X_test, Y_train, Y_test

def separateFeaturesAndTargets(df):
    X = df.drop(columns=["LoanApproved"])
    Y = df["LoanApproved"]

    return X, Y

def loadDataset(filename):
    df = pd.read_csv(filename)
    return df

def main():
    border = "-"*50
    print(border)
    print("Customer Loan Approval Case Study")
    print(border)

    # Step 1 : Load the dataset

    print(border)
    print("Step 1 : Load the dataset")
    print(border)

    df = loadDataset("Customer_Loan_Approval.csv")
    print("Dataset loaded successfully")
    print(border)

    print("First few records: ")
    print(df.head())
    print(border)

    print("Missing values of features:")
    print(df.isnull().sum())


    # Step 2 : Separate features and labels
    
    print(border)
    print("Step 2 : Separate features and labels")
    print(border)

    X, Y = separateFeaturesAndTargets(df)

    print("X shape is : ", X.shape)
    print("Y shape is : ", Y.shape)

    # Step 3 : Split the dataset
        
    print(border)
    print("Step 3 : Split the dataset")
    print(border)

    X_train, X_test, Y_train, Y_test = splitDataset(X, Y)

    print("Data splited into training and testing data")
    print(border)

    print("X train shape : ", X_train.shape)
    print("X test shape : ", X_test.shape)

    print("Y train shape :", Y_train.shape)
    print("Y test shape : ", Y_test.shape)

    # Step 4 : Train Logistic Regression model
        
    print(border)
    print("Step 4 : Train Logistic Regression model")
    print(border)

    model_logi = trainLogistics(X_train, Y_train)

    print("Logistics model created and trained successfully")

    # Step 5 : Train Decision Tree model
            
    print(border)
    print("Step 5 : Train Decision Tree model")
    print(border)

    model_tree = trainDecisionTree(X_train, Y_train)

    print("Decision tree classifier model created and trained successfully")
 
    # Step 6 : Train KNN model
             
    print(border)
    print("Step 6 : Train KNN model")
    print(border)   

    model_knn = trainKNN(X_train, Y_train)

    print("KNN model created and trained successfully")
     
    # Step 7 : calculate accuracies of all model
                 
    print(border)
    print("Step 7 : calculate accuracies of all model")
    print(border)

    accuracy_logi = calculateAccuracy(model_logi, X_test, Y_test)
    accuracy_tree = calculateAccuracy(model_tree, X_test, Y_test)
    accuracy_knn = calculateAccuracy(model_knn, X_test, Y_test)

    print("Accuracy of logistics model : ", accuracy_logi)
    print(border)
    print("Accuracy of Decision Tree model : ", accuracy_tree)
    print(border)
    print("Accuracy of KNN model : ", accuracy_knn)
    print(border)

    # Step 8 : Create Hard Voting classifier
                     
    print(border)
    print("Step 8 : Create Hard Voting classifier")
    print(border)

    model = buildVotingModel("hard")

    model = model.fit(X_train, Y_train)

    # Step 9 : Calculate accuracy for voting hard model
                         
    print(border)
    print("Step 9 : Calculate accuracy for voting hard model")
    print(border)

    accuracy_hard = calculateAccuracy(model, X_test, Y_test)

    print("Accuracy of Voting Hard classifier model : ", accuracy_hard)

    # Step 10 : Create Soft voting classifier
                         
    print(border)
    print("Step 10 : Create Soft voting classifier")
    print(border)

    model = buildVotingModel("soft")

    model = model.fit(X_train, Y_train)

    # Step 11 : Calculate accuracy for voting soft model
                         
    print(border)
    print("Step 11 : Calculate accuracy for voting soft model")
    print(border)

    accuracy_hard = calculateAccuracy(model, X_test, Y_test)

    print("Accuracy of Voting Soft classifier model : ", accuracy_hard)

    print(border)
    print("Accuracies of Decision Tree Classifier, Logistic model, KNN model, ensemble both soft and hard voting classifier model is same ie 100%")
    print(border)


if __name__ == "__main__":
    main()
