def main():
    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    border = "-"*50
    print(border)
    print("Calculate mean of X and Y: ")

    n = len(X)
    sum_X = 0
    sum_Y = 0

    for i in range(n):
        sum_X = sum_X + X[i]
        sum_Y = sum_Y + Y[i]

    mean_X = sum_X / n
    mean_Y = sum_Y / n

    print("Mean of X is : ", mean_X)
    print("Mean of Y is : ", mean_Y)
    print(border)

    print("Calculate coefficient ie m of X : ")

    #    m = sum( (X - meanX)(Y - meanY) ) / sum( (X - meanX)**2 )

    numerator = 0
    denomerator = 0

    for i in range(n):
        numerator = numerator + (X[i] - mean_X) * (Y[i] - mean_Y)
        denomerator = denomerator + (X[i] - mean_X) ** 2

    coefficient = numerator / denomerator

    print("Coefficient is : ", coefficient)
    print(border)

    print("Calculating intercept of Y ie c : ")

    #   y = mX + c

    #   meanY = m * meanX + c
    #   c =  meanY - m * meanX

    c = mean_Y - coefficient * mean_X 

    print("Intercept of Y ie c is : ", c)
    print(border)

    print("Predict the value of Y for 6 : ")

    #   y_pred = m * X + c

    y_pred = coefficient * 6 + c

    print("Predicted Y for X 6 : ", y_pred)

if __name__ == "__main__":
    main()