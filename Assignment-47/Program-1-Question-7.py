import numpy as np

from sklearn.linear_model import LinearRegression

def main():
    border = "-"*50

    X = np.array([
        [1],
        [2],
        [3],
        [4],
        [5]
    ])

    Y = np.array([
        50,
        55,
        60,
        65,
        70
    ])

    print("Independent variables are: ")
    print(X.tolist())
    print(border)

    print("Dependent variables are: ")
    print(Y)
    print(border)

    model = LinearRegression()

    model = model.fit(X, Y)

    print("Model trained successfully")
    print(border)
    print("Coefficient is : ", model.coef_)
    print("Intercept is : ", model.intercept_)
    print(border)

if __name__ == "__main__":
    main()