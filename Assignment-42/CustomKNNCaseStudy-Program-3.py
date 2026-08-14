import math

def sortDataset(dataset):
    sortedDataset = sorted(dataset, key= lambda data: data["distance"])

    print("Sorted data is : ")
    
    for data in sortedDataset:
        print(data)     

    return sortedDataset

def calculateEucliDistance(data1, data2):
    X = (data1["StudyHours"] - data2["StudyHours"])**2
    Y = (data1["Attendence"] - data2["Attendence"])**2

    return math.sqrt(X+Y)

def getDataSet():
    dataset = [
        {"StudyHours": 2, "Attendence": 60, "Result": "Fail"},
        {"StudyHours": 5, "Attendence": 80, "Result": "Pass"},
        {"StudyHours": 6, "Attendence": 85, "Result": "Pass"},
        {"StudyHours": 1, "Attendence": 50, "Result": "Fail"}
    ]

    return dataset

def getVotes(sortedDataset, K=3):
    nearest = sortedDataset[:K]
    
    votes = {}
    
    for nearData in nearest:
        label = nearData["Result"]
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
    print("Get study hours and attendence from user")
    print(border)

    studyHours = float(input("Enter study hours : "))
    attendence = float(input("Enter attendence : "))

    if studyHours <= 0.0:
        print("Invalid number for study hours. It should be greater than zero")
        return

    if (attendence <= 0.0):
            print("Invalid number for attendence. It should be greater than zero")
            return

    newData = {"StudyHours": studyHours, "Attendence": attendence}

    print("New data for which class to predict is : ", newData)
    print(border)

    print("Dataset with euclidean distance is: ")
    for data in dataset: 
        data["distance"] = calculateEucliDistance(data, newData)
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
    print("New input data  ", newData, " is of class ", classResult)
    print(border)

    

if __name__ == "__main__":
    main()