import numpy as np

# Step-1 : 5 * 5 matrix

image = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

filter = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
])

print("Original 5 * 5 image\n")
print(image)

print("Kernel 3 * 3\n")
print(filter)

# Step-2: Convolution operation
# feature map size = (((N - m)/stride) + 1) * (((N - m)/stride) + 1)
# 5-3/1 + 1 * 5-3/1 + 1= 3 *3

featureMap = np.zeros((3, 3))
for i in range(3):
    for j in range(3):
        region = image[i:i+3, j:j+3]
        result = np.sum(region * filter)
        featureMap[i][j] = result


print(featureMap)
