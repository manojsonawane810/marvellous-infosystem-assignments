import numpy as np
import math
from sklearn.preprocessing import StandardScaler

def calculateDistance(p1, p2):
    formula = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    distance = math.sqrt(formula)
    return distance

def main():
    border = "-"*50

    data = [
        [25, 20000],
        [30, 40000],
        [35, 80000]
    ]

    print(border)

    testData = [
        [40, 160000]
    ]

    print("Calculate the euclidean distances of all data point")
    print(border)

    distances = []

    for i in range(len(data)):
        p1 = data[i]
        p2 = testData[0]
        dis = calculateDistance(p1, p2)
        distances.append(dis)

    print("Distances are : ", distances)
    print(border)
    print("Scale the dataset using StandardScaler: ")
    scaler = StandardScaler()

    data_scaled = scaler.fit_transform(data)

    print("Scaled data is : ")
    print(data_scaled)

    print(border)
    print("Calculate the euclidean distances of on scale data points")
    print(border)
    scaler = StandardScaler()
    testData_scaled = scaler.fit_transform(testData)

    print("Scaled test data is : ", testData_scaled)
    print(border)

    distances = []
    
    for i in range(len(data_scaled)):
        p1 = data_scaled[i]
        p2 = testData_scaled[0]
        dis = calculateDistance(p1, p2)
        distances.append(dis)
    
    print("Distances are : ", distances)
    print(border)


    print("Calculate distances between 2 point from dataset: ")
    print(border)

    distance = calculateDistance(data[0], data[1])
    print("Distance before scalling is : ", distance)
    print(border)
    distance = calculateDistance(data_scaled[0], data_scaled[1])
    print("Distance after scalling is : ", distance)
    print(border)

    print("The difference in distances before and after scaling is due to scale change in the variables.")
    print("In the actual dataset, variables have extream different ranges in the values." \
    " Variable with larger values dominates the disctance calculation. So scaling bring them all to same range, " \
    " giving all variables equal importance.")

if __name__ == "__main__":
    main()