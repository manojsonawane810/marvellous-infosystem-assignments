import pandas as pd

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

    for i in range(len(dataframe)):
        sumOfmarks = 0
        for c in (dataframe.iloc[[i]]):
            if c != "Name":
                sumOfmarks = sumOfmarks + dataframe[c]    

    dataframe["Total"] = sumOfmarks
    
    print("Data with \"Total\" column is : ")
    print(dataframe)
    print(border)

    print("Shape of dataframe is ", dataframe.shape)
    print("Columns in dataframe are: ")
    print(dataframe.columns.tolist())
    print(border)

    dataframe = pd.DataFrame(data)

    dataframe["Total"] = dataframe[["Math", "Science", "English"]].sum(axis=1)
    print(dataframe)
    print(border)

    dataframe = pd.DataFrame(data)
    dataframe["Total"] = dataframe.sum(axis=1, numeric_only=True)
    print(dataframe)

    

if __name__ == "__main__":
    main()