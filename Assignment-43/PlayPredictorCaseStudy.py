import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def prepareDataset(dataset): 
    dataset.drop(dataset.columns[0], inplace=True, axis=1)   
    dataset.dropna(inplace=True)
    
    X = dataset.drop(columns=["Play"])
    Y = dataset["Play"]
    
    return X, Y

def loadDataset():
    return pd.read_csv("MarvellousInfosystems_PlayPredictor.csv")

def encodeFeatureData(data):
    encodedDataMap = {}

    for col in data:
        encoder = LabelEncoder()
        encodedData = encoder.fit_transform(data[col])
        data[col] = encodedData
        encodedDataMap[col] = encoder
    
    return data, encodedDataMap

def encodeTargetData(data):
    encodedDataMap = {}

    encoder = LabelEncoder()
    encodedData = encoder.fit_transform(data)
    encodedDataMap[data.name] = encoder

    return data, encodedDataMap

def trainTheModel(X, Y, K):
    model = KNeighborsClassifier(n_neighbors=K)
    
    model = model.fit(X, Y)

    return model

def testTheModel(model):
    test_data = {"Wether" : ["Sunny"], "Temperature": ["Hot"]}
    
    test_dataFrame = pd.DataFrame(test_data)
    
    encodedTestData, mapData = encodeFeatureData(test_dataFrame)
    
    return test_data, model.predict(encodedTestData)

def checkAccuracy(X, Y, K):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

    model = KNeighborsClassifier(n_neighbors = K)
    model = model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    print("Y_pred values :")
    print(list(Y_pred))

    accuracy = accuracy_score(Y_test, Y_pred)

    return accuracy
    
def main():
    border = "-"*50
    print(border)
    print("Marvellous Play Predictor System")
    print(border)

    #####################################################################
    # Step 1 : Load the dataset csv file
    #####################################################################

    print(border)
    print("Step 1 : Load the dataset csv file")
    print(border)

    dataset = loadDataset()
    
    print("Dataset shape is : ", dataset.shape)
    print("Some data records in dataset are : ")
    
    #df = dataset.drop()
    
    #####################################################################
    # Step 2 : Clean, prepare and manipulate dataW
    #####################################################################
    
    print(border)
    print("Step 2 : Clean, prepare and manipulate data")
    print(border)

    X, Y = prepareDataset(dataset)
    
    print("X shape is : ", X.shape)
    print("Y shape is : ", Y.shape)

    print("Feature columns are : " , X.columns.tolist())
    print("Target column is Play")

    #####################################################################
    # Step 3 : Encode the dataset
    #####################################################################

    print(border)
    print("Step 3 : Encode the dataset")
    print(border)

    X, encodedMap = encodeFeatureData(X)

    print("Encoded features are : ")

    for col, en in encodedMap.items():
        print(f"{col} {list(en.classes_)}")
        print("Encoded values are : ")
        print(f"{list(range(len(en.classes_)))}")
    
    print(border)

    #Y, encodedMap = encodeTargetData(Y)

    #print("Encoded targets are : ")
    
    #for col, en in encodedMap.items():
        #print(f"{col} {list(en.classes_)}")
        #print("Encoded values are : ")
        #print(f"{list(range(len(en.classes_)))}")
        
    #print(border)

    #####################################################################
    # Step 4 : Train the data
    #####################################################################
    
    print(border)
    print("Step 4 : Train the data")
    print(border)

    model = trainTheModel(X, Y, 3)
    
    print("Model trained successfully")
    print(border)

    #####################################################################
    # Step 5 : Test data
    #####################################################################
        
    print(border)
    print("Step 5 : Test data")
    print(border)

    test_data, Y_pred = testTheModel(model)

    print(f"The result of given wether and temperature {test_data} is : ")
    print(Y_pred[0])
    print(border)

    #####################################################################
    # Step 6 : Calculate Accuracy
    #####################################################################
            
    print(border)
    print("Step 6 : Calculate Accuracy")
    print(border)

    K = 5
    accuracy = checkAccuracy(X, Y, K)

    print("Accuracy of the model with K = ", K , " is : ", accuracy*100)
    print(border)
    print("Assignment 43 is completed!")
    print(border)

if __name__ == "__main__":
    main()