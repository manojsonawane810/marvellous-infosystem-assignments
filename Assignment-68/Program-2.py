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

rows, cols = featureMap.shape

for i in range(rows):
    for j in range(cols):

        if featureMap[i][j] >= 0:
            pass
        else:
            featureMap[i][j] = 0

print(featureMap)

pooling = np.zeros((2,2))

for i in range(2):
    for j in range(2):
        region = featureMap[i:i+2, j:j+2]
        print(region)
        pooling[i][j] = np.max(region)

        print("Pooling result : ")
        print(pooling)


