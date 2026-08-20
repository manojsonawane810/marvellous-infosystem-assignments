import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def main():
    X = np.array([
        [1],
        [2],
        [3],
        [4],
        [5]
    ])

    Y = np.array([
        20000,
        25000,
        30000,
        35000,
        40000
    ])

    border = "-"*50

    print("Independent variables are : ")
    print(X)
    print(border)

    print("Dependent varaibles are: ")
    print(Y)
    print(border)

    model = LinearRegression()

    model = model.fit(X, Y)

    print("Model built and trained successfully")
    print(border)
    input = [[6]]

    Y_pred = model.predict(input)

    print("Predicted salary for 6 years experience : ", Y_pred)
    print(border)

    print("Display plot : ")

    plt.figure(figsize=(7,5))

    x = np.linspace(1, 6, len(X)) # 2nd value canges line position, why?

    #plt.plot(X, Y, color="g", label="Regression Line") # changes line position, why?
    plt.plot(x, Y, color="g", label="Regression Line")
    plt.scatter(X, Y, color="r", label="Scatter plot")
    plt.xlabel("X : Independent varaibles")
    plt.ylabel("Y: Dependent variables")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()