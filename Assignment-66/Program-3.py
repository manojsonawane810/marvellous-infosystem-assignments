import numpy as np
import math 
def calculateMSE(Y_test, Y_pred):
    size = len(Y_pred)
    totalError = 0
    for i in range(size):
        totalError = totalError + ((Y_test[i] - Y_pred[i]) ** 2)

    mse = totalError / size
    return mse

def calculateBCE(Y_test, Y_pred):
    size = len(Y_pred)
    totalLoss = 0

    for i in range(size):
        error = (Y_test[i] * math.log(Y_pred[i])) + ((1 - Y_test[i]) * math.log(1 - Y_pred[i]))
        totalLoss = totalLoss + error

    BCE = - (totalLoss / size)
    return BCE

def main():
    Y_test = np.array([22, 33.5, 14.9, 44.7, 88.67, 33.2, 66.9])
    Y_pred = np.array([21, 33, 14.1, 44.2, 88.67, 33, 66.1])
    
    mse = calculateMSE(Y_test, Y_pred)
    print("Mean squared error is : ", mse)

    Y_test = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1])
    Y_pred = np.array([0.976, 0.2343, 0.5643, 0.6867, 0.886, 0.352, 0.3002, 0.73432, 0.23, 0.7, 0.8])

    bce = calculateBCE(Y_test, Y_pred)
    print("Binary cross entropy is : ", bce)

    print("Mean squared error function is used to calculate loss in case of regression models " \
    " where output is in the format of continuous numeric values of any range.")
    
    print("Binary cross entropy is used to measure how close the predicted" \
    " probability distribution is to the actual 0 or 1 labels")

if __name__ == "__main__":
    main()