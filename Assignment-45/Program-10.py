import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    border = "-"*50
    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82]
    }


    dataframe = pd.DataFrame(data)
    print("Data is : ")
    print(dataframe)
    print(border)

    print("Adding \"Total\" column for total of all marks in dataframe: ")
    print(border)
    dataframe["Total"] = dataframe[["Math", "Science", "English"]].sum(axis=1)
    print(border)
    

    print("Change the name \"Pooja\" to \"Puja\" : ")
    print(border)
    
    for i in range(len(dataframe)):
        for j in range(len(dataframe.columns)):
            if dataframe.columns[j] == "Name":
                if dataframe.iat[i, j] == "Pooja":
                    dataframe.iat[i, j] = "Puja"

    print(dataframe)
    print(border)

    print("Sorting the dataframe by Total column in descending order : ")

    dataframe = dataframe.sort_values(by=["Total"], ascending=False)
    print(dataframe)

    print(border)

    print("Create a bar plot of Student names vs total marks")
    print(border)
    plt.figure(figsize=(7,5))

    plt.bar(
        dataframe["Name"],
        dataframe["Total"],
        width=0.5,
        edgecolor = "black",
        linewidth = 1,
        alpha = 0.8,
        label = "Students"
    )

    plt.title("Assignment 44 Bar chart")
    plt.xlabel("Student Names")
    plt.ylabel("Total marks")
    plt.legend()
    #plt.show()

    print("Create a line chart of marks for Amit")
    print(border)
    print(dataframe.iloc[1][["Name"]])
    print(dataframe.iloc[1][["Math", "Science", "English"]])

    plt.figure(figsize=(7,5))

    plt.plot(
        dataframe.iloc[1][["Math", "Science", "English"]],
        marker = "o",
        linestyle = "--",
        linewidth=2,
        markersize = 7,
        label="Marks"

    )

    plt.title("Assignment 44 Line chart")
    plt.xlabel("Student Amit")
    plt.ylabel("Student marks")
    plt.grid()
    plt.legend()
    #plt.show()

    data2 = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [np.nan, 76, 88],
        "Science": [91, np.nan, 85]
    }

    

    dataframe2 = pd.DataFrame(data2)

    print("Data with missing values")
    print(dataframe2)
    print(border)

    dataframe2["Math"] = dataframe2["Math"].fillna(dataframe2["Math"].mean())
    dataframe2["Science"] = dataframe2["Science"].fillna(dataframe2["Science"].mean())

    print("Updated dataframe")
    print(dataframe2)
    print(border)
    
    print("Dropping the English column from original dataframe")
    print(border)
    dataframe = dataframe.drop(columns=["English"])

    print("Origional Dataframe")
    print(dataframe)

    print("Dataframe shape is : ", dataframe.shape)

    print(border)

    print("Min max scalling for Math feature: ")

    #   x = x - minX / maxX - minX;


    math_min = np.min(dataframe["Math"])
    math_max = np.max(dataframe["Math"])

    min_max_scale = {}

    for d in dataframe["Math"]:
        scaling = (d - math_min) / (math_max - math_min)
        print(scaling)
        min_max_scale[d] = scaling
    print(min_max_scale)
    print("Normalization of Math feature using min max scaling is : ")

    for scale in min_max_scale.keys():
        print(f"Score {scale} has scaling of : {min_max_scale[scale]}")

    print(border)

    print("Create Gender column : ")
    print(border)
    dataframe.insert(1, "Gender", ["Male", "Male", "Female"])
    print(dataframe)
    print(border)

    """ print("Perform one hot encoding on Gender column : ")

     dataframe = pd.get_dummies(dataframe, columns=["Gender"], drop_first= True, dtype=int)

    print("One hot encoding has been performed on Gender column : ")
    print(dataframe)
    print(border) """

    print("Group student by Gender: ") 
    print(border)
    data = dataframe.groupby(by=["Gender"])["Total"].mean()

    print("Average mark per Gender group : ")
    print(data)
    print(border)

    print("Plot a pie chart: ")

    data = {
        "Name": ["Amit", "Sagar", "Pooja"],
        "Math": [85, 90, 78],
        "Science": [92, 88, 80],
        "English": [75, 85, 82]
    }
    
    dataframe = pd.DataFrame(data)
    print("Data is: ")
    print(dataframe)
    print(border)

    plt.figure(figsize=(7,6))
    data = dataframe.iloc[1][["Math", "Science", "English"]]
    data.plot.pie(

        colors=["r", "g", "b"],
        labels=[dataframe.iloc[1]["Math"], dataframe.iloc[1]["Science"], dataframe.iloc[1]["English"]]
    )

    plt.title("Pie chart of marks for student Sagar")
    plt.legend()
    plt.show()
    print(border)

    print("Adding \"Total\" column for total of all marks in dataframe: ")
    print(border)
    dataframe["Total"] = dataframe[["Math", "Science", "English"]].sum(axis=1)
    print(dataframe)
    print(border)

    print("Adding status column : marks >= 250 : pass else fail: ")
    print(border)
    for i in range(len(dataframe["Total"])):
        if dataframe["Total"][i] >= 250:
            dataframe.loc[i, "Status"] = "Pass"
        else:
            dataframe.loc[i, "Status"] = "Fail"
    
    print(dataframe)
    print(border)

    print("Number of student passed are : ", len(dataframe.loc[dataframe["Status"] == "Pass"]))
    print(border)

    print("Exporting dataframe to CSV file : ")
    print(border)
    dataframe.to_csv("Dataframe.csv")
    print("Dataframe exported to CSV")
    print(border)

    print("Plot histogram of math")
    print(border)

    plt.hist(
        dataframe["Math"],
        bins= 5,
        color="skyblue",
        edgecolor="black"
    )    

    plt.title("Histogram of Math Marks")
    plt.xlabel("Math Marks")
    plt.ylabel("Frequency")
    plt.show()

    print("Feature \"Math\" has been renamed to \"Mathematics\" " )
    dataframe = dataframe.rename(columns={"Math": "Mathematics"})
    print(dataframe)
    print(border)

    print("Plot boxplot for English marks")

    sns.boxplot(
        x = "Status",
        y = "English",
        data= dataframe
    )

    plt.title("English mark boxplot: ")
    plt.show()
    
if __name__ == "__main__":
    main()