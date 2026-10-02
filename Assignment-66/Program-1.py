import math

def main():
    # input features x1, x2
    x1 = 2
    x2 = 3

    # features weights w1, w2
    w1 = 0.4
    w2 = 0.6

    # bias
    bias = 0.5

    # weightedSum = x1*w1 + x2*w2 + bias

    weightedSum = x1*w1 + x2*w2 + bias

    print("Weighted sum is : ", weightedSum)

    # Sigmoid activation funtion = 1 / (1 + e ^ - weightedSum)

    sigActivation = 1 / (1 + math.exp(-weightedSum))

    print("Sigmoid activation result is : ", sigActivation)

    if sigActivation > 0.5:
        print("Sigmoid activation output is close to 1 as value is greater than 0.5")
    else:
        print("Sigmoid activation output is close to 0 as value is less than 0.5")

if __name__ == "__main__":
    main()