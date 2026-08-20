import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    border = "-"*50

    data = [
        [25, 20000],
        [30, 40000],
        [35, 80000]
    ]

    print(border)
    print("Scale the dataset using StandardScaler: ")
    scaler = StandardScaler()

    data_scaled = scaler.fit_transform(data)

    print("Scaled data is : ")
    print(data_scaled)

if __name__ == "__main__":
    main()