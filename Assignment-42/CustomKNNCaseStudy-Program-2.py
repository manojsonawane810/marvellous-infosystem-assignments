import math

def sortDataset(dataset):
    sortedDataset = sorted(dataset, key= lambda data: data["distance"])

    print("Sorted data is : ")
    
    for data in sortedDataset:
        print(data)     

    return sortedDataset

def calculateEucliDistance(point1, point2):
    X = (point1["X"] - point2["X"])**2
    Y = (point1["Y"] - point2["Y"])**2

    return math.sqrt(X+Y)

def getDataSet():
    dataset = [
        {"Point": "A", "X": 1, "Y": 2, "Label": "Red"},
        {"Point": "B", "X": 2, "Y": 3, "Label": "Red"},
        {"Point": "C", "X": 3, "Y": 1, "Label": "Blue"},
        {"Point": "D", "X": 6, "Y": 5, "Label": "Blue"},
    ]

    return dataset

def getVotes(sortedDataset, K=3):
    nearest = sortedDataset[:K]
    
    votes = {}
    
    for nearData in nearest:
        label = nearData["Label"]
        votes[label] = votes.get(label, 0) + 1

    return votes

def getMaxVotedClass(votes):
    maxVote = 0
    classResult = ""
    
    for vote in votes:
        if votes[vote] >= maxVote:
            maxVote = votes[vote]
            classResult = vote

    return classResult

def main():
    border= "-"*50

    print(border)
    print("Custom KNN case study")
    print(border)

    dataset = getDataSet()

    print("Dataset is : ")

    for data in dataset:
        print(data)

    print(border)
    print("Get X and Y coordinates from user")
    print(border)

    XCord = float(input("Enter X  coordinate : "))
    YCord = float(input("Enter Y coordinate : "))

    if (XCord <= 0):
        print("Invalid X coordinate. It should be greater than zero")
        return

    if (YCord <= 0):
            print("Invalid Y coordinate. It should be greater than zero")
            return

    newPoint = {"X": XCord, "Y": YCord}

    print("New point for which class to predict is : ", newPoint)
    print(border)

    print("Dataset with euclidean distance is: ")
    for data in dataset: 
        data["distance"] = calculateEucliDistance(data, newPoint)
        print(data)

    print(border)

    sortedDataset = sortDataset(dataset)

    print(border)

    # Number of nearest distances to consider
    K = 3

    # get voting based on nearest distances 
    votes = getVotes(sortedDataset, K)

    print("Voting is : ", votes)
    print(border)

    classResult = getMaxVotedClass(votes)

    print("Predicted class label is ", classResult)
    print("New point ", newPoint, " is of class ", classResult)
    print(border)

    print("Predict the class of same new point with different K values 1, 3 and 5")
    print(border)
    K = 1

    print("Predicting using K = 1")
    print(border)

    votes = getVotes(sortedDataset, K)
    print("Voting is ", votes)
    
    classResult = getMaxVotedClass(votes)

    print(f"When K = {K}, predicted class label is ", classResult)
    print(border)

    K = 3

    print("Predicting using K = 3")
    print(border)

    votes = getVotes(sortedDataset, K)
    print("Voting is ", votes)

    classResult = getMaxVotedClass(votes)

    print(f"When K = {K}, predicted class label is ", classResult)
    print(border)

    K = 5

    print("Predicting using K = 5")
    print(border)

    votes = getVotes(sortedDataset, K)
    print("Voting is ", votes)

    classResult = getMaxVotedClass(votes)
    print(f"When K = {K}, predicted class label is ", classResult)
    print(border)

    print("When K increases, then depending on the dataset size the prediction changes becasue there is not sufficient number of data in dataset. " \
    "Due to which voting generated the same voting result or equal result. So the prediction has changed.")

if __name__ == "__main__":
    main()