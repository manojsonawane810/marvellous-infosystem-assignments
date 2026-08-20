import numpy as np

def main():
    data = [6, 7, 8, 9, 10, 11, 12]

    border = "-"*50
    print(border)
    print("Calculate mean of dataset :")
    print(border)

    dataset = np.array(data)
    print("Dataset is : ")
    print(dataset)
    print(border)

    meanData = np.mean(dataset)

    print("Mean is : ", meanData)
    print(border)

    deviation = np.std(dataset)
    print("Standard deviation of the dataset is: ", deviation)
    print(border) 

    variance = np.var(data)
    print("Variance is : ", variance)   


if __name__ == "__main__":
    main()