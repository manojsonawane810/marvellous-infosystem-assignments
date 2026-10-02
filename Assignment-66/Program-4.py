import random

# Input

x = 3

# Tager

y = 10

print("Input value : ", x)
print("Expected value : ", y)

# Initial weight

w = random.uniform(0, 1)

# bias

b = 0.2

learning_rate = 0.1

print("Inital weight is : ", w)
print("Bias is : ", b)
print("Learning rate is : ", learning_rate)

# store details

stepsList = []
lossList = []
weightList = []
predictionList = []

for step in range(1, 15):
    print(f"\n------------------Step {step} -------------")

    # Forward pass
    predictedOutput = x * w + b
    print("Predicted output : ", predictedOutput)

    # Error
    error = y - predictedOutput
    print("Error is : ", error)

    # loss
    loss = error ** 2
    print("Loss is : ", loss)

    # Store values

    stepsList.append(step)
    lossList.append(loss)
    weightList.append(w)
    predictionList.append(predictedOutput)

    w = w + (learning_rate * error * x)
    print("Updated weight : ", w)

print("Final result is: ")

finalOutput = x * w + b

print("Final output is : ", finalOutput)
print("Expected out is : ", y)
print("Final weight is : ", w)

