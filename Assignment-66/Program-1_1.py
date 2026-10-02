import numpy as np
import math

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def main():
    x1 = 2
    x2 = 3

    inputs = np.array([x1, x2])

    w1 = 0.4
    w2 = 0.6

    weights = np.array([w1, w2])

    bias = 0.5

    print("Inputs : ", inputs)
    print("Weights : ", weights)

    weightedSum = np.dot(inputs, weights) + bias

    weightedSum = sum(x * w for x, w in zip(inputs, weights)) + bias

    print("Weighted sum is : ", weightedSum)

    y = sigmoid(weightedSum)

    print("Final output : ", y)

    if y > 0.5:
        print("Sigmoid activation output is close to 1 as value is greater than 0.5")
    else:
        print("Sigmoid activation output is close to 0 as value is less than 0.5")
    
if __name__ == "__main__":
    main()