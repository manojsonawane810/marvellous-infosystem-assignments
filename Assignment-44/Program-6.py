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

if __name__ == "__main__":
    main()