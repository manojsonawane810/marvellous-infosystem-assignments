import numpy as np
from sklearn.linear_model import LinearRegression

def main():
    X = np.array([
        [1, 7],
        [2, 6],
        [3, 7],
        [4, 6],
        [5, 8]
    ])

    Y = np.array([
        [50],
        [55],
        [60],
        [65],
        [70]
    ])

    print(len(X[0]))

    border = "-"*50
    print("Independent variables are : ")
    print(X.tolist())
    print(border)

    print("Dependent varaibles are: ")
    print(Y.tolist())
    print(border)

    model = LinearRegression()

    model = model.fit(X, Y)

    print("Model build and trained successfully")
    print(border)

    coefficients = model.coef_

    for i in range(len(coefficients[0])):
        print("Coefficent of feature ", i+1 ," is: ", coefficients[0][i] )

    print(border)

    print("Intercept of y ie c is : ", model.intercept_)
    print(border)
    print("Practicle assignment 47 is completed")
    print(border)

if __name__ == "__main__":
    main()
    