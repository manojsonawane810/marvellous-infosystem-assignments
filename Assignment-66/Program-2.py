import numpy as np
import math
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

def sigmoid(x):
    return (1 / (1 + math.exp(-x)))

def tanh(x):
    return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x)) 

def plotFunction(input, output, title):
    plt.figure(figsize=(8,6))
    plt.plot(input, output, label = "Relu(x) = max(0, x)", color = "blue", linewidth = 2)
    plt.title(title, fontsize = 14)
    plt.xlabel("Input (x) ", fontsize = 12)
    plt.ylabel("Output (f(x)) ", fontsize = 12)
    plt.grid(True, which="both", linestyle=":", alpha=0.5)
    plt.legend(fontsize=12)
    plt.show()

def main():
    inputs = np.linspace(-10, 10, 20)
    print("Inputs are : ", inputs)

    outputs = relu(inputs)
    print("Relu output is : ", outputs)

    sigOutput = []
    tanhOutput = []
    for z in inputs:
        sigOutput.append(sigmoid(z))
        tanhOutput.append(tanh(z))

    print("Sigmoid output is : ", sigOutput)
    print("Tanh output is : ", tanh)

    print("Plot All Activation functions ")

    plotFunction(inputs, outputs, "Relu Activation Function Plot")
    plotFunction(inputs, sigOutput, "Sigmoid Activation Function Plot")
    plotFunction(inputs, tanhOutput, "Tanh Activation Function Plot")

    print("Use of each activation function: ")

    print("Relu: Relu is used mostly in hidden layers to modify the negative values" \
    " to positive zero and get the same value if positive. " \
    " This is very easy function and adds not linearity")

    print("Sigmoid: Sigmoid is mostly used if output classes are of binary type " \
    " where output would be either positive or negative. " \
    "The sigmoid output range is from 0 to 1. This is mostly used in output layer.")

    print("Tanh : Tanh is mostly used when we have output values ranging from negatives to positives. The range is from -1 to 1. Mostly used when we need output to zero centered. ")


if __name__ == "__main__":
    main()