import numpy as np

input = np.array([
    [6, 4],
    [8, 6]
])
print("Original array \n ")
print(input)

flattenArray = input.flatten()
print("Flatten array \n")
print(flattenArray)

weights = np.array([
    [0.5,  1.0, -0.5,  0.0],
    [0.0,  0.5,  1.0, -1.0]
])

biases = np.array([1.0, 2.0])

final_output = np.dot(weights, flattenArray) + biases

print("Finak result is : ")

print(final_output)




