import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def loadDataset():
    df = pd.read_csv("Fraudulent_Transaction_Detection.csv")
    return df

def convertCategoricals(df):
    df = pd.get_dummies(
        columns=["DeviceType"],
        data=df,
        dtype=int,
        drop_first=True
    )

    return df

def separateFeaturesAndLabels(df):
    X = df.drop(columns=["Fraud"])
    Y = df["Fraud"]
    return X, Y

def splitDataset(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
    return X_train, X_test, Y_train, Y_test

def scaleData(X_train, X_test):
    scaler = StandardScaler()
    
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.fit_transform(X_test)
    return X_train, X_test  

def buildDetModel():
    model_det = DecisionTreeClassifier(random_state=42)
    return model_det

def buildBaggingModel(base_model):
    model_bagg = BaggingClassifier(
        estimator=base_model,
        n_estimators=10,
        random_state=42
    )
    
    return model_bagg

def buildRandomForestModel():
    model_rand = RandomForestClassifier(
        n_estimators=10,
        random_state=42
    )
    return model_rand

def buildAdaBoostModel():
    model_boost = AdaBoostClassifier(
        learning_rate=1.0,
        n_estimators=20,
        random_state=42
    )
    return model_boost

def buildVotinBagging():

    model_det = buildDetModel()

    model_logi = LogisticRegression(
        max_iter=1000,
        random_state=42
    )

    model_knn = KNeighborsClassifier(
        n_neighbors=5,
    )

    model = VotingClassifier(
        estimators=[
            ("log", model_logi),
            ("det", model_det),
            ("knn", model_knn)
        ],
        voting="hard"
    )

    return model

def trainModel(model, X_train, Y_train):
    model = model.fit(X_train, Y_train)
    return model

def testModel(model, X_test):
    Y_pred = model.predict(X_test)
    return Y_pred

def evaluateModel(border, modelName, Y_test, Y_pred):
    print(f"Accuracy of {modelName} model is : ", accuracy_score(Y_test, Y_pred) * 100)
    print(border)
    print("Classification report is : ")
    print(classification_report(Y_test, Y_pred))
    print(border)
    print("Confusion matrix is : ")
    print(confusion_matrix(Y_test, Y_pred))
    print(border)
    

def main():
    border = "-"*50
    print(border)
    print("Fraudulent Transaction Detection Case Study")
    print(border)

    # Step 1 : Load the dataset
    print(border)
    print("Step 1 : Load the dataset")
    print(border)

    df = loadDataset()
    print("Dataset loaded, few entries are : ")
    print(df.head())
    print(border)
    print("Shape of dataset : ", df.shape)
    print(border)

    print("Missing values : ")
    print(df.isnull().sum())
    print(border)
        
    # Step 2 : Seprate independent and dependent variables

    print(border)
    print("Seprate independent and dependent variables")
    print(border)

    X, Y = separateFeaturesAndLabels(df)
    
    print("X shape : ", X.shape)
    print("Y shape : ", Y.shape)
    print(border)

    # Step 3 : Split the dataset
    print(border)
    print("Split the dataset")
    print(border)

    X_train, X_test, Y_train, Y_test = splitDataset(X, Y)    

    print("X train shape : ", X_train.shape)
    print("X test shape : ", X_test.shape)
    print("Y train shape : ", Y_train.shape)
    print("Y test shape : ", Y_test.shape)
    print(border)

    # Step 4 :  Creating Decision tree classifer model and evalute it
    print(border)
    print("Creating Decision tree classifer model and evalute it")
    print(border)

    model_det = buildDetModel()

    model_det = trainModel(model_det, X_train, Y_train)

    Y_pred = testModel(model_det, X_test)

    evaluateModel(border, "Decision Tree Classifier", Y_test, Y_pred)

    X_train, X_test = scaleData(X_train, X_test)

    # Step 5 : Bagging Classifier model and evalute it
    
    print(border)
    print("Bagging Classifier model and evalute it")
    print(border)

    base_model = buildDetModel()
    model = buildBaggingModel(base_model)

    model = trainModel(model, X_train, Y_train)

    Y_pred = testModel(model, X_test)

    evaluateModel(border, "Bagging Classifier", Y_test, Y_pred)


    # Step 6 : Random Forest model and evaluate it

    print(border)
    print("Random Forest model and evaluate it")
    print(border)
    
    model = buildRandomForestModel()
    model = trainModel(model, X_train, Y_train)
    
    Y_pred = testModel(model, X_test)

    evaluateModel(border, "Random Forest Classifier", Y_test, Y_pred)

    # Step 7 : Ada Boost model and evaluate it
    print(border)
    print("Ada Boost model and evaluate it")
    print(border)
    
    model = buildAdaBoostModel()
    model = trainModel(model, X_train, Y_train)
        
    Y_pred = testModel(model, X_test)

    evaluateModel(border, "Ada Boost Classifier", Y_test, Y_pred)

    # Step 7 : Voting Classifer model and evaluate it

    print(border)
    print("Voting Classifer model and evaluate it")
    print(border)

    model = buildVotinBagging()

    model = trainModel(model, X_train, Y_train)
            
    Y_pred = testModel(model, X_test)

    evaluateModel(border, "Voting Classifier", Y_test, Y_pred)

    print("Accuracy of Random Forest Classifier ensemble model is higher ie 100 % than other ensemble models")
    print("Accuracies of other models are same ie 97.44%")

if __name__ == "__main__":
    main()